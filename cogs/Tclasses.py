from sys import exc_info
from copy import deepcopy
from textwrap import shorten
from asyncio import sleep, TimeoutError
from contextlib import suppress
from typing import List

from discord import (
    Message, TextChannel,
    Forbidden, NotFound)
from discord.utils import get
from discord.ext.commands import Context
from discord.ext.commands.cog import Cog
from discord_components import Button
from NHentai.nhentai_async import NHentaiAsync as NHentai, Doujin

from utils.classes import Embed, Bot, BotInteractionCooldown
from utils.misc import (
    language_to_flag, 
    render_date, 
    is_int, is_float,
    restricted_tags)
from cogs.localization import *

newline = "\n"

class Classes(Cog):
    def __init__(self, bot):
        self.bot = bot

class ImagePageReader:
    def __init__(self, bot: Bot, ctx: Context, images:list, name:str, code:str, **kwargs):
        """Create and run a reader based on pages from a Doujin. 
        To work for any purpose, this class needs a few changes.
        
        `bot` - The Bot class created on initialization
        `ctx` - Context used
        `images` The list of image urls to use
        `name` - Title of the reader
        `code` - Book/Item ID

        `**kwargs` - Further keyword arguments if need be
        -- `current_page` - The starting page as an integer. Defaults to `0`

        """
        self.bot = bot
        self.ctx: Context = ctx
        self.images: list = images
        self.name: str = name
        self.code: str = code

        self.current_page: int = kwargs.pop("starting_page", 0)
        self.active_message: Message = None

        self.am_embed: Embed = None
        self.am_channel: TextChannel = None
        self.is_paused: bool = False
        self.on_bookmarked_page: bool = False

        self.language = self.bot.user_data["UserData"][str(ctx.author.id)]["Settings"]["Language"]

    async def update_reader(self):
        if self.code in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Bookmarks|*n*|bm'] and \
            self.current_page == self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Bookmarks|*n*|bm'][self.code]:
            self.on_bookmarked_page = True
        else:
            self.on_bookmarked_page = False

        self.am_embed.description = f"<:nprev:853668227124953159>{'<:nfini:853670159310913576>' if self.current_page == (len(self.images)-1) else '<:nnext:853668227207790602>'} {localization[self.language]['page_reader']['description']['previous']} | {localization[self.language]['page_reader']['description']['finish'] if self.current_page == (len(self.images)-1) else localization[self.language]['page_reader']['description']['next']}\n" \
                                    f"<:nsele:853668227212902410><:nstop:853668227175546952> {localization[self.language]['page_reader']['description']['select']} | {localization[self.language]['page_reader']['description']['stop']}\n" \
                                    f"<:npaus:853668227234529300><:nbook:853668227205038090> {localization[self.language]['page_reader']['description']['pause']} | {localization[self.language]['page_reader']['description']['bookmark'] if not self.on_bookmarked_page else localization[self.language]['page_reader']['description']['unbookmark']}\n" 

        self.am_embed.set_thumbnail(url=self.images[self.current_page+1].src if (self.current_page+1) in range(0, len(self.images)) else Embed.Empty)                
        self.am_embed.set_image(url=self.images[self.current_page].src)
        self.am_embed.set_footer(text=localization[self.language]['page_reader']['footer'].format(current=self.current_page+1, total=len(self.images), bookmark='🔖' if self.on_bookmarked_page else ''))

        if self.active_message:
            await self.active_message.edit(embed=self.am_embed,
                components=[
                    [Button(emoji=self.bot.get_emoji(853668227124953159), style=2, id="previous", disabled=self.current_page==0),
                    Button(emoji=self.bot.get_emoji(853670159310913576) if self.current_page+1==len(self.images) else self.bot.get_emoji(853668227207790602), style=2, id="next"),
                    Button(emoji=self.bot.get_emoji(853668227212902410), style=2, id="select"),
                    Button(emoji=self.bot.get_emoji(853668227175546952), style=2, id="stop"),
                    Button(emoji=self.bot.get_emoji(853668227234529300), style=2, id="pause")],
                    [Button(emoji=self.bot.get_emoji(853668227205038090), style=2, id="bookmark"),
                    Button(emoji="⭐", style=2, id="favorite"),
                    Button(label=localization[self.language]['page_reader']['redirect_button'], style=5, url="https://discord.gg/DJ4wdsRYy2")]])
        else:
            await self.ctx.send(embed=self.am_embed,
            components=[
                [Button(emoji=self.bot.get_emoji(853668227124953159), style=2, id="previous", disabled=self.current_page==0),
                Button(emoji=self.bot.get_emoji(853670159310913576) if self.current_page+1==len(self.images) else self.bot.get_emoji(853668227207790602), style=2, id="next"),
                Button(emoji=self.bot.get_emoji(853668227212902410), style=2, id="select"),
                Button(emoji=self.bot.get_emoji(853668227175546952), style=2, id="stop"),
                Button(emoji=self.bot.get_emoji(853668227234529300), style=2, id="pause")],
                [Button(emoji=self.bot.get_emoji(853668227205038090), style=2, id="bookmark"),
                Button(emoji="⭐", style=2, id="favorite"),
                Button(label=localization[self.language]['page_reader']['redirect_button'], style=5, url="https://discord.gg/DJ4wdsRYy2")]])

    async def setup(self):
        edit = await self.ctx.send(embed=Embed(
            description=f"{self.bot.get_emoji(810936543401213953)}"))

        # Fetch existing category for readers, otherwise create new
        cat = get(self.ctx.guild.categories, name="📖NReader")
        if not cat:
            cat = await self.ctx.guild.create_category_channel(name="📖NReader")
        elif not cat.permissions_for(self.ctx.guild.me).manage_roles:
            with suppress(Forbidden):
                await cat.delete()
            
            cat = await self.ctx.guild.create_category_channel(name="📖NReader")

        # Create reader channel under category
        channel = await cat.create_text_channel(name=f"📖nreader-{self.ctx.message.id}", nsfw=True)

        # Set channel permissions
        await channel.set_permissions(self.ctx.guild.me, read_messages=True)
        await channel.set_permissions(self.ctx.guild.default_role, read_messages=False)
        await channel.set_permissions(self.ctx.author, read_messages=True)

        self.am_embed = Embed(
            description=localization[self.language]['page_reader']['init']['description'])
        self.am_embed.set_author(
            name=f"{self.code} [*n*] {self.name}",
            icon_url="https://cdn.discordapp.com/emojis/845298862184726538.png?v=1")
        self.am_embed.set_footer(
            text=localization[self.language]['page_reader']['init']['footer'].format(total=len(self.images)))
        
        # Reader message
        conf = await channel.send( 
            content=self.ctx.author.mention, embed=self.am_embed,
            components=[Button(label="Start", style=1, emoji=self.bot.get_emoji(853674277416206387), id="button1")])

        # Portal
        await edit.edit(
            content=conf.channel.mention, 
            embed=Embed(
                description=localization[self.language]['page_reader']['portal'].format(code=self.code, name=self.name)
                ).set_author(
                    name=self.bot.user.name,
                    icon_url=self.bot.user.avatar_url),
            delete_after=10)

        while True:
            try:
                interaction = await self.bot.wait_for("button_click", timeout=30, bypass_cooldown=True,
                    check=lambda i: 
                        i.message.id == conf.id and \
                        i.user.id == self.ctx.author.id)
        
            except TimeoutError:
                with suppress(NotFound):
                    await conf.edit(content=f"{self.bot.get_emoji(810936543401213953)} {localization[self.language]['page_reader']['closing']}", embed=None)
            
                await sleep(1)
                
                with suppress(NotFound):
                    await conf.channel.delete()
                
                return False
        
            else:
                try: await interaction.respond(type=6)
                except Exception: continue
            
                self.active_message = conf
                self.am_channel = conf.channel

                await self.update_reader()

                await sleep(0.2)

                return True

    async def start(self):
        if self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["enabled"]:
            while self.code in self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"]:
                self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"].remove(self.code)

            self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"].insert(0, self.code)

            if "0" in self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"]:
                self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"].remove("0")
            
            if len(self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"]) >= 2 and \
                self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"][1] == self.code:
                self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"].pop(0)
            
            while len(self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"]) > 25:
                self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"].pop()

            if "0" not in self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"]:
                self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["History|*n*|his"]["list"].append("0")
        
        while True:
            try:
                interaction = await self.bot.wait_for("button_click", timeout=60*5,
                    check=lambda i: i.message.id==self.active_message.id and i.user.id==self.ctx.author.id)

            except TimeoutError:
                with suppress(NotFound):
                    self.am_embed.set_image(url=Embed.Empty)
                    self.am_embed.set_thumbnail(url=Embed.Empty)
                    self.am_embed.description=localization[self.language]['page_reader']['timeout'].format(current=self.current_page+1, total=len(self.images))

                    await self.active_message.edit(embed=self.am_embed, components=[])
                    temp = await self.am_channel.send(content=localization[self.language]['page_reader']['timeout_notification'].format(mention=self.ctx.author.mention, delete_after=1))
                    await temp.delete(delay=1)
        
                    await sleep(10)

                    with suppress(NotFound):
                        await self.active_message.edit(content=f"{self.bot.get_emoji(810936543401213953)} {localization[self.language]['page_reader']['closing']}", embed=None)

                    await sleep(1)
                    await self.am_channel.delete()

                    break
            
            except BotInteractionCooldown:
                continue
            
            else:
                try:
                    try: await interaction.respond(type=6)
                    except NotFound: continue

                    self.bot.inactive = 0
                    if interaction.component.id == "next":  # Next page
                        self.current_page = self.current_page + 1
                        if self.current_page > (len(self.images)-1):  # Finish the doujin if at last page
                            self.am_embed.set_image(url=Embed.Empty)
                            self.am_embed.set_thumbnail(url=Embed.Empty)
                            self.am_embed.description=localization[self.language]['page_reader']['finished']

                            await self.active_message.edit(embed=self.am_embed, components=[])
                            if self.code in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Read Later|*n*|rl']:
                                self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Read Later|*n*|rl'].remove(self.code)
                            
                            await sleep(2)
                            await self.active_message.edit(content=f"{self.bot.get_emoji(810936543401213953)} {localization[self.language]['page_reader']['closing']}", embed=None)

                            await sleep(1)
                            await self.am_channel.delete()
                            
                            break
                        else:
                            await self.update_reader()

                    elif interaction.component.id == "previous":  # Previous page
                        if self.current_page == 0:  # Not allowed to go behind zero
                            continue
                        else:
                            self.current_page = self.current_page - 1
                        
                        await self.update_reader()
                    
                    elif interaction.component.id == "select":  # Select page
                        bm_page = None
                        if self.code in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Bookmarks|*n*|bm']:
                            bm_page = self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Bookmarks|*n*|bm'][self.code]
                        
                        conf = await self.am_channel.send(embed=Embed(
                            description=localization[self.language]['page_reader']['select_inquiry']['description']
                        ).set_footer(
                            text=localization[self.language]['page_reader']['select_inquiry']['footer'].format(bookmarked_page=f"**{bm_page+1}**" if bm_page else 'N/A')))
                        
                        while True:
                            try:
                                m = await self.bot.wait_for("message", timeout=15, bypass_cooldown=True,
                                    check=lambda m: m.author.id == self.ctx.author.id and m.channel.id == self.am_channel.id)
                            
                            except TimeoutError:
                                await conf.delete()
                                break

                            else:
                                with suppress(Forbidden):
                                    await m.delete()
                                
                                if m.content == "n-cancel":
                                    await conf.delete()
                                    break
                                
                                if is_int(m.content) and (int(m.content)-1) in range(0, len(self.images)):
                                    await conf.delete()
                                    self.current_page = int(m.content)-1
                                    
                                    await self.update_reader()
                                    
                                    break
                                
                                else:
                                    with suppress(Forbidden):
                                        await m.delete()

                                    continue
                    
                    elif interaction.component.id == "pause":  # Pause and send to recall
                        self.am_embed.set_image(url=Embed.Empty)
                        self.am_embed.set_thumbnail(url=Embed.Empty)
                        self.am_embed.description=localization[self.language]['page_reader']['paused']
                        
                        await self.active_message.edit(embed=self.am_embed, components=[])

                        await sleep(2)
                        await self.active_message.edit(content=f"{self.bot.get_emoji(810936543401213953)} {localization[self.language]['page_reader']['closing']}", embed=None)
                        
                        await sleep(1)
                        await self.am_channel.delete()
                        
                        await sleep(1)
                        self.bot.user_data["UserData"][str(self.ctx.author.id)]["Recall"] = f"{self.code}*n*{self.current_page}"
                        await self.ctx.author.send(embed=Embed(
                            title=localization[self.language]['page_reader']['recall_saved']['title'],
                            description=localization[self.language]['page_reader']['recalled']['description'].footer(code=self.code, current=self.current_page+1, total=len(self.images))))

                        break

                    elif interaction.component.id == "stop":  # Stop entirely
                        self.am_embed.set_image(url=Embed.Empty)
                        self.am_embed.set_thumbnail(url=Embed.Empty)
                        self.am_embed.description=localization[self.language]['page_reader']['stopped']
                        
                        await self.active_message.edit(embed=self.am_embed, components=[])

                        await sleep(2)
                        await self.active_message.edit(content=f"{self.bot.get_emoji(810936543401213953)} {localization[self.language]['page_reader']['closing']}", embed=None)
                        
                        await sleep(1)
                        await self.am_channel.delete()
                        
                        break
                    
                    elif interaction.component.id == "bookmark":  # Set/Remove bookmark
                        if not self.on_bookmarked_page:
                            if self.current_page == 0:
                                await self.am_channel.send(
                                    embed=Embed(
                                        color=0xFF0000,
                                        description=localization[self.language]['page_reader']['cannot_bookmark_first_page']
                                    ),
                                    delete_after=5)
                                continue

                            if len(self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["Bookmarks|*n*|bm"]) >= 25: 
                                await self.am_channel.send(
                                    color=0xff0000, 
                                    embed=Embed(
                                        description=localization[self.language]['page_reader']['bookmarks_full']
                                    ),
                                    delete_after=5)
                                continue

                            self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Bookmarks|*n*|bm'][self.code] = self.current_page
                            self.on_bookmarked_page = True
                        
                        else:
                            if self.code in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Bookmarks|*n*|bm']:
                                self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Bookmarks|*n*|bm'].pop(self.code)
                                self.on_bookmarked_page = False
                        
                        await self.update_reader()

                    elif interaction.component.id == "favorite":  # Add to favorites
                        if len(self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["Bookmarks|*n*|bm"]) >= 25: 
                            await self.am_channel.send(
                                color=0xff0000, 
                                embed=Embed(
                                    description=localization[self.language]['page_reader']['favorites_full']
                                ),
                                delete_after=5)
                            continue

                        if self.code not in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Favorites|*n*|fav']:
                            self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Favorites|*n*|fav'].append(self.code)

                            await self.am_channel.send(
                                embed=Embed(
                                    description=localization[self.language]['page_reader']['added_to_favorites']
                                ),
                                delete_after=5)
                        else:
                            self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']['Favorites|*n*|fav'].remove(self.code)

                            await self.am_channel.send(
                                embed=Embed(
                                    description=localization[self.language]['page_reader']['removed_from_favorites']),
                                delete_after=5)

                except Exception:
                    error = exc_info()
                    temp = await self.am_channel.send(embed=Embed(
                        color=0xFF0000,
                        description=localization[self.language]['page_reader']['error']),
                        delete_after=10)
                    
                    await temp.delete(delay=10)
                        
                    await self.bot.errorlog.send(error, ctx=self.ctx, event="ImagePageReader")
                    
                    continue

        return

class SearchResultsBrowser:
    def __init__(self, bot: Bot, ctx: Context, results: List[Doujin], **kwargs):
        """Class to create and run a browser from NHentai-API

        `results` - obtained from nhentai_api.search(query)
        `msg` - optional message that the bot owns to edit, otherwise created 
        """
        self.bot = bot
        self.ctx = ctx
        self.doujins = results
        self.index = 0
        self.lolicon_allowed = kwargs.pop("lolicon_allowed", False)
        self.minimal_details = kwargs.pop("minimal_details", True)
        self.name = kwargs.pop("name", "Search Results")

        self.active_message: Message = kwargs.pop("msg", None)
        self.am_embed: Embed = None

        self.language = self.bot.user_data["UserData"][str(ctx.author.id)]["Settings"]["Language"]
    
    async def update_browser(self, ctx):
        message_part = []
        for ind, dj in enumerate(self.doujins):
            try: 
                if ind == self.index and int(dj.id) in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']["Favorites|*n*|fav"]: symbol = '🟩'
                elif ind == self.index: symbol='🟥'
                elif int(dj.id) in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']["Favorites|*n*|fav"]: symbol = '🟦'
                else: symbol='⬛'
            except KeyError: 
                symbol='⬛'
            
            tags = [tag.name for tag in dj.tags if tag.type == "tag"]
            if any([tag in restricted_tags for tag in tags]) and ctx.guild and not self.lolicon_allowed:
                message_part.append(
                    f"{'**' if ind == self.index else ''}"
                    f"`{symbol} {str(ind+1).ljust(2)}` | __`       `__ | ⚠🚫 | Contains restricted tags."
                    f"{'**' if ind == self.index else ''}")
            else:
                message_part.append(
                    f"{'**' if ind == self.index else ''}"
                    f"`{symbol} {str(ind+1).ljust(2)}` | "
                    f"__`{str(dj.id).ljust(7)}`__ | "
                    f"{language_to_flag(dj.languages)} | "
                    f"{shorten(dj.title.pretty, width=40, placeholder='...')}"
                    f"{'**' if ind == self.index else ''}")
                
        self.am_embed = Embed(
            title=self.name,
            description=f"\n"+('\n'.join(message_part))+"\n\n▌█████████████████▓▓▒▒░░")
        
        nhentai = NHentai()
        doujin = self.doujins[self.index]
        
        tags = [tag.name for tag in doujin.tags if tag.type == "tag"]
        if any([tag in restricted_tags for tag in tags]) and self.ctx.guild and not self.lolicon_allowed:
            self.am_embed.add_field(
                name="Forbidden",
                inline=False,
                value="⚠️❌ This doujin cannot be viewed in this server."
            ).set_footer(
                text=f"⭐ N/A"
            )
            
            doujin.cover.src = str(self.bot.user.avatar_url)
        
        else:
            if self.minimal_details:
                self.am_embed.add_field(
                    name="Minimal Details",
                    inline=False,
                    value=
                        f"ID: `{doujin.id}`\n"
                        f"{localization[self.language]['doujin_info']['fields']['title']}: {language_to_flag(doujin.languages)} `{shorten(doujin.title.pretty, width=256, placeholder='...')}`\n"
                        f"{localization[self.language]['doujin_info']['fields']['artists']}: `{', '.join([tag.name for tag in doujin.artists]) if doujin.artists else localization[self.language]['doujin_info']['fields']['not_provided']}`\n"
                        f"{localization[self.language]['doujin_info']['fields']['characters']}: `{', '.join([tag.name for tag in doujin.characters]) if doujin.characters else localization[self.language]['doujin_info']['fields']['original']}`\n"
                        f"{localization[self.language]['doujin_info']['fields']['parodies']}: `{', '.join([tag.name for tag in doujin.parodies]) if doujin.parodies else localization[self.language]['doujin_info']['fields']['original']}`\n"
                        f"{localization[self.language]['doujin_info']['fields']['tags']}:\n||`{shorten(str(', '.join([tag.name for tag in doujin.tags if tag.type == 'tag']) if [tag.name for tag in doujin.tags if tag.type == 'tag'] else localization[self.language]['doujin_info']['fields']['not_provided']), width=950, placeholder='...')}`||"
                ).set_footer(
                    text=f"{localization[self.language]['doujin_info']['sfw']}")

                self.am_embed.set_author(
                    name=f"NHentai",
                    icon_url="https://cdn.discordapp.com/emojis/845298862184726538.png?v=1")

                await self.active_message.edit(content="", embed=self.am_embed)

            else:
                self.am_embed.add_field(
                    name=localization[self.language]['doujin_info']['fields']['title'],
                    inline=False,
                    value=f"`{shorten(doujin.title.pretty, width=256, placeholder='...')}`"
                ).add_field(
                    inline=False,
                    name=localization[self.language]['doujin_info']['fields']['id/pages'],
                    value=f"`{doujin.id}` - `{doujin.total_pages}`"
                ).add_field(
                    inline=False,
                    name=localization[self.language]['doujin_info']['fields']['date_uploaded'],
                    value=f"`{render_date(doujin.upload_at, self.language)}`"
                ).add_field(
                    inline=False,
                    name=localization[self.language]['doujin_info']['fields']['languages'],
                    value=f"{language_to_flag(doujin.languages)} `{', '.join([localization[self.language]['doujin_info']['fields']['language_names'][tag.name] for tag in doujin.languages]) if doujin.languages else localization[self.language]['doujin_info']['fields']['not_provided']}`"
                ).add_field(
                    inline=False,
                    name=localization[self.language]['doujin_info']['fields']['artists'],
                    value=f"`{', '.join([tag.name for tag in doujin.artists]) if doujin.artists else localization[self.language]['doujin_info']['fields']['not_provided']}`"
                ).add_field(
                    inline=False,
                    name=localization[self.language]['doujin_info']['fields']['characters'],
                    value=f"`{', '.join([tag.name for tag in doujin.characters]) if doujin.characters else localization[self.language]['doujin_info']['fields']['original']}`"
                ).add_field(
                    inline=False,
                    name=localization[self.language]['doujin_info']['fields']['parodies'],
                    value=f"`{', '.join([tag.name for tag in doujin.parodies]) if doujin.parodies else localization[self.language]['doujin_info']['fields']['original']}`"
                ).set_footer(
                    text=f"⭐ {doujin.total_favorites}"
                )

                # Doujin count for tags
                tags_list = []
                for tag in [tag for tag in doujin.tags if tag.type == "tag"]:
                    count = tag.count
                    parse_count = list(str(count))
                    if len(parse_count) < 4:
                        tags_list.append(f"{localization[self.language]['fields']['tag_names'][tag.name] if tag.name in localization[self.language]['doujin_info']['fields']['tag_names'] else tag.name}[{count}]")
                    elif len(parse_count) >= 4 and len(parse_count) <= 6:
                        count = count/1000
                        tags_list.append(f"{localization[self.language]['fields']['tag_names'][tag.name] if tag.name in localization[self.language]['doujin_info']['fields']['tag_names'] else tag.name}[{round(count, 1)}k]")
                    elif len(parse_count) > 7:
                        count = count/1000000
                        tags_list.append(f"{localization[self.language]['fields']['tag_names'][tag.name] if tag.name in localization[self.language]['doujin_info']['fields']['tag_names'] else tag.name}[{round(count, 2)}m]")

                self.am_embed.add_field(
                    inline=False,
                    name=localization[self.language]["doujin_info"]["fields"]["tags"],
                    value=f"```{shorten(str(', '.join(tags_list) if tags_list else localization[self.language]['doujin_info']['fields']['not_provided']), width=1018, placeholder='...')}```"
                )

                self.am_embed.set_author(
                    name=f"NHentai",
                    url=f"https://nhentai.net/g/{doujin.id}/",
                    icon_url="https://cdn.discordapp.com/emojis/845298862184726538.png?v=1")
                self.am_embed.set_thumbnail(url=doujin.images[0].src)
            
        previous_emb = deepcopy(self.am_embed)
        if previous_emb.image.url != Embed.Empty:
            self.am_embed.set_image(url=doujin.cover.src)
            self.am_embed.set_thumbnail(url=Embed.Empty)
        elif previous_emb.thumbnail != Embed.Empty:
            self.am_embed.set_thumbnail(url=doujin.cover.src)
            self.am_embed.set_image(url=Embed.Empty)
        else:  # Image wasn't set yet
            self.am_embed.set_thumbnail(url=doujin.cover.src)

        self.active_message.embeds[0] = self.am_embed

        if not self.active_message:
            self.active_message = await self.ctx.send("...")

        if not self.ctx.guild or (self.ctx.guild and not all([
            ctx.guild.me.guild_permissions.manage_channels, 
            ctx.guild.me.guild_permissions.manage_roles, 
            ctx.guild.me.guild_permissions.manage_messages])):
            await self.active_message.edit(
                embed=self.am_embed,
                components=[
                    [Button(emoji=self.bot.get_emoji(853800909108936754), style=2, id="up"),
                    Button(emoji=self.bot.get_emoji(853800909276315678), style=2, id="down"),
                    Button(emoji=self.bot.get_emoji(853668227212902410), style=2, id="select"),
                    Button(emoji=self.bot.get_emoji(853668227175546952), style=2, id="stop"),
                    Button(emoji=self.bot.get_emoji(853684136379416616), style=2, id="read", disabled=True)],
                    [Button(emoji=self.bot.get_emoji(853684136433942560), style=2, id="zoom", disabled=self.minimal_details),
                    Button(emoji=self.bot.get_emoji(853668227205038090), style=2, id="readlater"),
                    Button(label="Support Server", style=5, url="https://discord.gg/DJ4wdsRYy2")]]),

        else:
            await self.active_message.edit(
                embed=self.am_embed,
                components=[
                    [Button(emoji=self.bot.get_emoji(853800909108936754), style=2, id="up"),
                    Button(emoji=self.bot.get_emoji(853800909276315678), style=2, id="down"),
                    Button(emoji=self.bot.get_emoji(853668227212902410), style=2, id="select"),
                    Button(emoji=self.bot.get_emoji(853668227175546952), style=2, id="stop"),
                    Button(emoji=self.bot.get_emoji(853684136379416616), style=2, id="read", disabled=self.minimal_details)],
                    [Button(emoji=self.bot.get_emoji(853684136433942560), style=2, id="zoom", disabled=self.minimal_details),
                    Button(emoji=self.bot.get_emoji(853668227205038090), style=2, id="readlater"),
                    Button(label="Support Server", style=5, url="https://discord.gg/DJ4wdsRYy2")]]),
            
            await sleep(0.5)
    
    async def start(self, ctx):
        """Initial start of the result browser."""

        await self.update_browser(self.ctx)

        while True:
            try:
                interaction = await self.bot.wait_for("button_click", timeout=300, 
                    check=lambda i: \
                        i.message.id == self.active_message.id and \
                        i.user.id == self.ctx.author.id)
            except TimeoutError:
                message_part = []
                for ind, dj in enumerate(self.doujins):
                    tags = [tag.name for tag in dj.tags if tag.type == "tag"]
                    if any([tag in restricted_tags for tag in tags]) and ctx.guild and not self.lolicon_allowed:
                        message_part.append("__`       `__ | ⚠🚫 | Contains restricted tags.")
                    else:
                        message_part.append(
                            f"__`{str(dj.id).ljust(7)}`__ | "
                            f"{language_to_flag(dj.languages)} | "
                            f"{shorten(dj.title.pretty, width=50, placeholder='...')}")
                
                self.am_embed = Embed(
                    title=self.name,
                    description=f"\n"+('\n'.join(message_part)))
                self.am_embed.set_author(
                    name="NHentai",
                    url=f"https://nhentai.net/",
                    icon_url="https://cdn.discordapp.com/emojis/845298862184726538.png?v=1")
                

                self.am_embed.set_thumbnail(url=Embed.Empty)
                self.am_embed.set_image(url=Embed.Empty)

                await self.active_message.edit(embed=self.am_embed, components=[])
                
                return

            except BotInteractionCooldown:
                continue
            
            else:
                try: await interaction.respond(type=6)
                except NotFound: continue

                try:
                    self.bot.inactive = 0
                    
                    if interaction.component.id == "up":
                        if self.index > 0:
                            self.index -= 1
                            await self.update_browser(self.ctx)
                        elif self.index == 0:
                            self.index = len(self.doujins)-1
                            await self.update_browser(self.ctx)

                    elif interaction.component.id == "down":
                        if self.index < len(self.doujins)-1:
                            self.index += 1
                            await self.update_browser(self.ctx)
                        elif self.index == len(self.doujins)-1:
                            self.index = 0
                            await self.update_browser(self.ctx)
                    
                    elif interaction.component.id == "select":
                        conf = await self.ctx.send(embed=Embed(
                            description="Enter a result number within 15 seconds, or type `n-cancel` to cancel.\n"))

                        while True:
                            try:
                                m = await self.bot.wait_for("message", timeout=15, bypass_cooldown=True,
                                    check=lambda m: m.author.id == self.ctx.author.id and m.channel.id == self.ctx.channel.id)
                            
                            except TimeoutError:
                                break

                            else:
                                with suppress(Forbidden):
                                    await m.delete()
                                
                                if m.content == "n-cancel":
                                    await conf.delete()
                                    break
                                
                                if is_int(m.content) and (int(m.content)-1) in range(0, len(self.doujins)):
                                    await conf.delete()
                                    self.index = int(m.content)-1
                                    await self.update_browser(self.ctx)
                                    break

                                else:
                                    continue
                    
                    elif interaction.component.id == "stop":
                        message_part = []
                        for ind, dj in enumerate(self.doujins):
                            tags = [tag.name for tag in dj.tags if tag.type == "tag"]
                            if any([tag in restricted_tags for tag in tags]) and ctx.guild and not self.lolicon_allowed:
                                message_part.append("__`       `__ | ⚠🚫 | Contains restricted tags.")
                            else:
                                message_part.append(
                                    f"__`{str(dj.id).ljust(7)}`__ | "
                                    f"{language_to_flag(dj.languages)} | "
                                    f"{shorten(dj.title.pretty, width=50, placeholder='...')}")
                        
                        self.am_embed = Embed(
                            title=self.name,
                            description=f"\n"+('\n'.join(message_part)))

                        self.am_embed.set_author(
                            name="NHentai",
                            url=f"https://nhentai.net/",
                            icon_url="https://cdn.discordapp.com/emojis/845298862184726538.png?v=1")
                        
                        self.am_embed.set_thumbnail(url=Embed.Empty)
                        self.am_embed.set_image(url=Embed.Empty)
                        await self.active_message.edit(embed=self.am_embed, components=[])
                        
                        return
                    
                    elif interaction.component.id == "read":
                        tags = [tag.name for tag in self.doujins[self.index].tags if tag.type == "tag"]
                        if any([tag in restricted_tags for tag in tags]) and ctx.guild and not self.lolicon_allowed:
                            continue
                        
                        message_part = []
                        for ind, dj in enumerate(self.doujins):
                            tags = [tag.name for tag in dj.tags if tag.type == "tag"]
                            if any([tag in restricted_tags for tag in tags]) and ctx.guild and not self.lolicon_allowed:
                                message_part.append("__`       `__ | ⚠🚫 | Contains restricted tags.")
                            else:
                                message_part.append(
                                    f"{'**' if ind == self.index else ''}"
                                    f"__`{str(dj.id).ljust(7)}`__ | "
                                    f"{language_to_flag(dj.languages)} | "
                                    f"{shorten(dj.title.pretty, width=50, placeholder='...')}"
                                    f"{'**' if ind == self.index else ''}")

                        self.am_embed = Embed(
                            title=self.name,
                            description=f"\n"+('\n'.join(message_part)))
                        self.am_embed.set_author(
                            name="NHentai",
                            url=f"https://nhentai.net/",
                            icon_url="https://cdn.discordapp.com/emojis/845298862184726538.png?v=1")
                        
                        self.am_embed.set_thumbnail(url=Embed.Empty)
                        self.am_embed.set_image(url=Embed.Empty)

                        await self.active_message.edit(content='', embed=self.am_embed, components=[])

                        doujin = self.doujins[self.index]
                        if str(doujin.id) in self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']["Bookmarks|*n*|bm"]:
                            page = self.bot.user_data['UserData'][str(self.ctx.author.id)]['Lists']['Built-in']["Bookmarks|*n*|bm"][str(doujin.id)]
                        else:
                            page = 0

                        session = ImagePageReader(self.bot, ctx, doujin.images, doujin.title.pretty, str(doujin.id), starting_page=page)
                        response = await session.setup()
                        if response:
                            await session.start()
                        else:
                            await self.active_message.edit(embed=self.am_embed)

                        return
                    
                    elif interaction.component.id == "zoom":
                        emb = deepcopy(self.am_embed)
                        if not emb.image:
                            self.am_embed.set_image(url=emb.thumbnail.url)
                            self.am_embed.set_thumbnail(url=Embed.Empty)
                        elif not emb.thumbnail:
                            self.am_embed.set_thumbnail(url=emb.image.url)
                            self.am_embed.set_image(url=Embed.Empty)
                        
                        await self.active_message.edit(embed=self.am_embed)

                    elif interaction.component.id == "readlater":
                        if len(self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["Read Later|*n*|rl"]) >= 25: 
                            await self.ctx.send(
                                embed=Embed(
                                    color=0xff0000, 
                                    description="❌ Your Read Later list is full. Please remove something from it to perform this action."
                                ),
                                delete_after=5)
                            continue

                        if str(self.doujins[self.index].id) not in self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["Read Later|*n*|rl"]:
                            self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["Read Later|*n*|rl"].append(str(self.doujins[self.index].id))
                            await self.ctx.send(
                                embed=Embed(
                                    description=f"✅ Added `{self.doujins[self.index].id}` to your Read Later list."
                                ),
                                delete_after=5)
                        else:
                            self.bot.user_data["UserData"][str(self.ctx.author.id)]["Lists"]["Built-in"]["Read Later|*n*|rl"].remove(str(self.doujins[self.index].id))
                            await self.ctx.send(
                                embed=Embed(
                                    description=f"✅ Removed `{self.doujins[self.index].id}` from your Read Later list."
                                ),
                                delete_after=5)
            
                except Exception:
                    error = exc_info()
                    temp = await self.ctx.send(
                        embed=Embed(
                            color=0xFF0000,
                            description="An unhandled error occured; Please try again.\n"
                                        "If the issue persists, please try searching again.\n"
                                        "If searching again doesn't work, click the `Support Server` button."
                        ).set_footer(text="This message will disappear in 10 seconds."),
                        delete_after=10)
                        
                    await self.bot.errorlog.send(error, ctx=self.ctx, event="SearchResultsBrowser")
                    
                    continue

def setup(bot):
    bot.add_cog(Classes(bot))
