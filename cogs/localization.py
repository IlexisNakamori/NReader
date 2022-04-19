localization = {
	"eng": {
		"language_not_available": {
			"description": 
				"This command isn't available in the language you selected. Continue?",
			"footer":
				"You can help translate NReader by visiting the support guild.",
			"button": 
				"Continue"
		},
		"language_options": {
			"english": 
				"English",
			"japanese":
				"Japanese",
			"chinese":
				"Chinese"
		},
		"general": {
			"not_nsfw": 
				"❌ This command cannot be used in a non-NSFW channel.",
		},

		"notifications_due": {
			"first_time_tip": {
				"title":
					"First Time Interaction Notification",
				"description":
					"👋 It appears to be your first time using this bot!\n"
					"🔞 This bot is to be used by mature users only and in NSFW channels.\n"
					"ℹ️ For more information and help, please use the `n!help` command.\n"
					"ℹ️ For brief legal information, please use the `n!legal` command.\n"
					"ℹ️ MechHub highly recommends you join the support server: **[MechHub/DJ4wdsRYy2](https://discord.gg/DJ4wdsRYy2)**\n"
			},

			"lolicon_viewing_tip": 
				"Tip: To view restricted doujins on Discord, you need to invite me to a server that you own and run the `n!whitelist <'add' or 'remove'>` (Server-owner only) command. \n"
				"This will allow all users in your server to open restricted doujins.\n"
				"Restricted doujins are __only__ reflected on your history, favorites, bookmarks, or searches **in whitelisted servers**, but numerical statistics *may not* hide these ouside those domains."
		},

		"help": {
			"title": 
				"<:info:818664266390700074> Help",
			"description": 
				"**Search, overview, and read doujins in Discord.**\n" 
				"**Support server: [MechHub/DJ4wdsRYy2](https://discord.gg/DJ4wdsRYy2)**\n" 
				"\n" 
				"For the full information sheet, visit [this Google Docs page](https://docs.google.com/document/d/e/2PACX-1vQAJRI5B8x0CP3ZCHjK9iZ8KQq3AGHEMwiBQL72Mwf1Zu6N2THedbAi1ThuB9iiuzcBv8ipt5_XfQf4/pub).\n"
				"\n"
				"Changing the bot language will also reset first time notifications.", 
			"footer": 
				"Provided by MechHub"
		},

		"invite": {
			"title": 
				"Invite NReader",
			"description": 
				"[Click Here]({url}) to invite NReader to your server!",
			"footer": 
				"Provided by MechHub"
		},

		"privacy": {
			# English only
		}, 

		"doujin_info": {
			"sfw":
				"Showing minimal information. Use the command in an NSFW-marked channel for more details.",
			"not_a_valid_id": 
				"❌ You didn't type a proper ID. Come on, numbers!",
			"doujin_not_found": 
				"🔎❌ I did not find a doujin with that ID.",
			"is_lolicon":
				"⚠️⛔ This doujin contains restricted tags and cannot be displayed publically.",
			"fields": {
				"not_provided":
					"Not provided",
				"original":
					"Original",

				"title": 
					"Title",

				"id/pages":
					"ID || Pages",

				"date_uploaded":
					"Date uploaded",
				"date_uploaded_weekdays": {
					0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
					4: "Thursday", 5: "Friday", 6: "Saturday"
				},

				"languages":
					"Language(s) in this work",
				"language_names": {
					"translated": "Translated",
					"rewrite": "Rewritten",
					"speechless": "No dialogue",
					"text cleaned": "Text Removed",
					"japanese": "Japanese",
					"english": "English",
					"chinese": "Chinese",
					"cebuano": "Cebuano",
					"arabic": "Arabic",
					"javanese": "Javanese"
				},

				"artists":
					"Featured artist(s)",

				"characters":
					"Character(s) in this work",

				"parodies":
					"A parody of",

				"tags": 
					"Content tags",
				"tag_names": {},  # Translate a bunch of different common tags
			},

			"read": 
				"Read",
			"expand_thumbnail":
				"Expand Thumbnail",
			"minimize_thumbnail":
				"Minimize Thumbnail",
			"need_permissions":
				"Need Permissions",
			"unexpected_loss":
				"❌ Unexpected loss of required permissions.",
			"opened":
				"Opened"
		},
		
		"page_reader": { 
			"description": {
				"previous":
					"Previous",
				"next": 
					"Next",
				"finish":
					"**Finish**",
				"select":
					"Select",
				"stop":
					"Stop",
				"pause":
					"Pause",
				"bookmark":
					"Bookmark",
				"unbookmark":
					"Unbookmark"
			},
			"footer": 
				"Page [{current}/{total}] {bookmark}",
			"redirect_button":
				"Support Server",
			"init": {
				"description":
					"Waiting.",
				"footer":
					"Page [0/{total}]: Press ▶ Start to start reading.",
				"button":
					"Start",
			},
			"portal":
				"Click/Tap the mention above to jump to your reader.\n"
				"You opened `{code}`: `{name}`",
			"closing":
				"Closing...",
			"timeout":
				"You timed out on page [{current}/{total}].",
			"timeout_notification":
				"{mention}, you timed out in your doujin. Forgot to press pause?",
			"finished":
				"You finished this doujin.",
			"select_inquiry": {
				"description":
					"Use the numbered buttons to enter a page number.\n"
					"[◀ = Backspace] [🗑 = Cancel] [✅ = Enter] [🔖 = Bookmark]",
				"footer":
					"Bookmarked page: {bookmarked_page}",
			},
			"paused":
				"You paused this doujin.",
			"recall_saved": {
				"title":
					"Recall saved.",
				"description": 
					"Doujin `{code}` saved to recall to page [{current}/{total}].\n"
					"To get back to this page, run the `n!recall` command to instantly open a new reader starting on that page.",
			},
			"stopped":
				"You stopped reading this doujin.",
			"cannot_bookmark_first_page":
				"You cannot bookmark the first page. Use favorites instead!",
			"bookmarks_full":
				"❌ Your Bookmarks list is full. Please remove something from it to perform this action.",
			"favorites_full":
				"❌ Your Favorites list is full. Please remove something from it to perform this action.",
			"added_to_favorites":
				"✅ Added `{code}` to your favorites.",
			"removed_from_favorites":
				"✅ Removed `{code}` from your favorites.",
			"error":
				"An unhandled error occured; Please try again.\n"
				"If the issue persists, please try reopening the doujin.\n"
				"If reopening doesn't work, click the `Support Server` button."
		},

		"search_doujins": {  
			"searching": 
				"<a:nreader_loading:810936543401213953> Searching...\n"
				"```\n"
				"{query} {appendage}\n"
				"```\n",

			"invalid_page": {
				"title":
					"❌ Invalid page number.",
				"description":
					"`0` (zero) is not a valid page number. Page number must be greater than zero."
			},
			"invalid_sort": {
				"title":
					"❌ Invalid sort parameter.",
				"description":
					"That's not a method I can sort by. I can only support by popularity `today`, this `week`, this `month`, all time `popular` (default), or `recent`."
			},
			"too_broad": {
				"title":
					"❌ Search is too broad. Say something.",
				"description":
					"You need to tell me what to search, or update your search appendage (See `search_appendage` in `n!help`)."
			},
			"unexpected_error":
				"❌ There was an unexpected error in your search. Typically, retrying doesn't work, so please try another search.",
			"no_results": {
				"title":
					"🔎❌ I did not find anything. Check your keywords!",
				"description": {
					"appendage": 
						"`*️⃣` This may be the cause of your search appendage. See `search_appendage` in `n!help`, or add `--noappend` to bypass it.",
					"page":
						"`*️⃣` You have added a page number to your search (`--page#`). Please check that your page is within the total page count (check by searching without a page).",
					"restricted_tags":
						"`*️⃣` You searched for restricted tags. Due to the way this bot works, restricted tags get cancelled out, resulting in a null search."
				}
			},

			"search_results": {
				"title":
					"Search Results",
				"description":
					"Showing page {page}/{pages} (~{approximate} doujins):\n"
					"{results}",
			},
			"contains_restricted_tags":
				"__`       `__ | ⚠🚫 | Contains restricted tags.",
			"start_interactive":
				"Start Interactive"
		},

		"results_browser": { # Over half of what would be here actually uses the doujin_info material
			"buttons": {
				"select":
					"Use the numbered buttons to enter a result number.\n"
					"[◀ = Backspace] [🗑 = Cancel] [✅ = Enter]",
				"read_later_full":
					"❌ Your Read Later list is full. Please remove something from it to perform this action.",
				"add_to_read_later":
					"✅ Added `{code}` to your Read Later list.",
				"remove_from_read_later":
					"✅ Removed `{code}` from your Read Later list.",
				"support_server":
					"Support Server"
			},
			"forbidden": {
				"title":
					"Forbidden",
				"description":
					"⚠️❌ This doujin cannot be viewed in this server."
			},
			"minimal_details": 
				"Minimal Details"
		},

		"recall": {
			
		},

		"popular": {
			
		},

		"lists": {
			
		},

		"recommend": {
			
		},

		"search_appendage": {
		
		},

		"whitelist": {
			
		},

		"urban_dictionary": {
			# English only
		}

	},

	"jp": {
		"language_not_available": {
			"description": 
				"このコマンドは、ご使用の言語では使用できません。 継続する？",
			"footer": 
				"サポートギルドにアクセスすると、NReaderの翻訳を手伝うことができます。",
			"button": 
				"継続"
		},
		"language_options": {
			"english": 
				"英語",
			"japanese":
				"日本語",
			"chinese":
				"中国語"
		},

		"notifications_due": {
			"first_time_tip": {
				"title":
					"初回インタラクション通知",
				"description":
					"👋 ボットを初めて使用したようです！\n"
					"🔞 このボットは大人専用で、NSFWチャンネルでのみ使用できます。\n"
					"ℹ️ 詳細については、「`n!help`」コマンドを使用してください。 \n"
					"ℹ️ 英語の法律情報については、「`n!legal`」コマンドを使用してください。\n"
					"ℹ️ MechHubは、サポートギルドに参加することを強くお勧めします: **[MechHub/DJ4wdsRYy2](https://discord.gg/DJ4wdsRYy2)**\n"
			},

			"lolicon_viewing_tip": 
				"ヒント：Discordで制限付き成人雜誌を表示するには、サーバーに招待して、「`n！whitelist <'add'または 'remove'>`」コマンドを実行します。"
                "これにより、サーバー上のすべてのユーザーが制限付き成人雜誌を開くことができます。\n"
                "制限付き成人雜誌は、ホワイトリストに登録されたサーバーでの履歴、お気に入り、ブックマーク、または検索にのみ反映されますが、数値統計ではこれらのドメインの外にそれらを隠すことはできません。"
		},

		"help": {
			"title": 
				"<:info:818664266390700074> 手助け",
			"description": 
				"**Discordで成人雜誌を検索、概要、読みます。**\n" 
				"**サポートギルド: [MechHub/DJ4wdsRYy2](https://discord.gg/DJ4wdsRYy2)**\n" 
				"\n" 
				"すべての情報については、この[Googleドキュメント](https://docs.google.com/document/d/e/2PACX-1vSZkUzrO5sbwWJJPdejrn_Kl_HEsEqBjzTotcTmEI7bfcS8NDB4FDJnhEO2-avYCVuSMHThozw3H81b/pub)にアクセスしてください。\n"
				"\n"
				"ボットの言語を変更すると、初回の通知もリセットされます。",
			"footer": 
				"MechHubから提供された"
		},

		"invite": {
			"title": 
				"NReaderを招待する",
			"description": 
				"NReaderをギルドに招待するには、ここを[クリック]({url})してください。",
			"footer": 
				"MechHubから提供された"
		},

		"doujin_info": {
			"sfw":
				"最小限の情報を表示しています。 詳細については、NSFWでマークされたチャンネルでコマンドを使用してください。",
			"not_a_valid_id": 
				"❌ 識別は番号ではありません。 数字のみ！",
			"doujin_not_found": 
				"🔎❌ ボットは、そのIDを持つ成人雜誌を見つけることができませんでした。",
			"is_lolicon":
				"⚠️⛔ この成人雜誌には許可されていないタグがあり、表示できません。",
			"fields": {
				"not_provided":
					"提供されていない",
				"original":
					"オリジナル",

				"title": 
					"題名",

				"id/pages":
					"身元 || ページ",

				"date_uploaded":
					"アップロード日",
				"date_uploaded_weekdays": {
					0: "日", 1: "月", 2: "火", 3: "水",
					4: "木", 5: "金", 6: "土"
				},

				"languages":
					"成人雜誌言語",
				"language_names": {
					"translated": "翻訳",
					"rewrite": "リライト",
					"speechless": "対話なし",
					"text cleaned": "テキストが削除",
					"japanese": "日本語",
					"english": "英語",
					"chinese": "中国語",
					"cebuano": "セブアノ語",
					"arabic": "アラビア語",
					"javanese": "ジャワ語"
				},

				"artists":
					"成人雜誌アーティスト",

				"characters":
					"成人雜誌キャラクター",

				"parodies":
					"成人雜誌パロディー",

				"tags": 
					"コンテンツタグ",
				"tag_names": {},  # Translate a bunch of different common tags
			},

			"read": 
				"読む",
			"expand_thumbnail":
				"イ表紙画像を展開",
			"minimize_thumbnail":
				"表紙画像を最小化",
			"need_permissions":
				"必要な権限 ",
			"unexpected_loss":
				"❌ 必要な権限の予期しない喪失。",
			"opened":
				"開いた"
		},
		
		"page_reader": { 
			"description": {
				"previous":
					"前",
				"next": 
					"次",
				"finish":
					"**終了**",
				"select":
					"選択",
				"stop":
					"やめる",
				"pause":
					"一時停止",
				"bookmark":
					"ブックマーク",
				"unbookmark":
					"ブックマーク解除"
			},
			"footer": 
				"ページ [{current}/{total}] {bookmark}",
			"redirect_button":
				"サポートギルド",
			"init": {
				"description":
					"待っている。",
				"footer":
					"ページ [0/{total}]：▶スタートを押して読み始めます。",
				"button":
					"スタート",
			},
			"portal":
				"上記の説明をクリック/タップして、読者にジャンプしてください。\n"
				"「`{code}`」を開きました： `{name}` ",
			"closing":
				"閉鎖...",
			"timeout":
				"[{current} / {total}] ページでタイムアウトしました。",
			"timeout_notification":
				"{mention}, 成人雜誌でタイムアウトしました。一時停止を押すのを忘れましたか？",
			"finished":
				"あなたはこの成人雜誌を完成させました。",
			"select_inquiry": {
				"description":
					"番号付きのボタンを使用して、ページ番号を入力します\n"
					"[◀=バックスペース] [🗑=キャンセル] [✅=入力] [🔖=ブックマーク]",
				"footer":
					"ブックマークされたページ：{bookmarked_page}",
			},
			"paused":
				"この成人雜誌を一時停止しました。",
			"recall_saved": {
				"title":
					"保存されたリコール。",
				"description": 
					"コード「`{code}`」が保存された成人雜誌は、ページ[{current}/{total}]に呼び戻すことができます。\n"
					"このページに戻るには、「`n!recall`」コマンドを実行して、そのページから始まる新しいリーダーをすぐに開きます。",
			},
			"stopped":
				"あなたはこの成人雜誌を読むのをやめました。",
			"cannot_bookmark_first_page":
				"最初のページをブックマークすることはできません。代わりにお気に入りを使用してください！",
			"bookmarks_full":
				"❌ ブックマークリストがいっぱいです。このアクションを実行するには、ブックマークリストから何かを削除してください。",
			"favorites_full":
				"❌ お気に入りリストがいっぱいです。このアクションを実行するには、リストから何かを削除してください。",
			"added_to_favorites":
				"✅ お気に入りに「`{code}`」を追加しました。",
			"removed_from_favorites":
				"✅ お気に入りから` 「{code}」 `を削除しました。",
			"error":
				"未処理のエラーが発生しました。もう一度やり直してください。\n"
				"問題が解決しない場合は、成人雜誌を再度開いてみてください。\n"
				"再度開くことができない場合は、「サポートギルド」ボタンをクリックしてください。"
		},

		"search_doujins": {  
			"searching": 
				"<a:nreader_loading:810936543401213953> サーチ...\n"
				"```\n"
				"{query} {appendage}\n"
				"```\n",

			"invalid_page": {
				"title":
					"❌ ページ番号が無効です。",
				"description":
					"`0` (ゼロ) は有効なページ番号ではありません。 ゼロより大きくなければなりません。"
			},
			"invalid_sort": {
				"title":
					"❌ ソートパラメータが無効です。",
				"description":
					"`today`、`week`、`month`、`popular`（デフォルト）、`recent` でしか並べ替えることができません。"
			},
			"too_broad": {
				"title":
					"❌ 検索範囲が広すぎます。",
				"description":
					"何を検索するか教えてください。 また、 `n！help` の下の `check_appendage` を確認してください。"
			},
			"unexpected_error":
				"❌ 予期しないエラー。 別の検索を試してください。",
			"no_results": {
				"title":
					"🔎❌ 結果がありません。",
				"description": {
					"appendage": 
						"`*️⃣` これが検索付属物の原因である可能性があります。 `n！help` の下の `search_appendage` を参照するか、`--noappend` を追加してバイパスします。",
					"page":
						"`*️⃣` 検索にページ番号を追加しました（`--page=＃`）。 ページが合計ページ数の範囲内であることを確認してください（ページなしで検索して確認してください）。",
					"restricted_tags":
						"`*️⃣` 制限付きタグを検索しました。 このボットの動作方法により、制限されたタグはキャンセルされ、検索がnullになります。"
				}
			},

			"search_results": {
				"title":
					"の検索結果",
				"description":
					"表示中のページ{page}/{pages}（〜{approximate}成人雜誌）:\n"
					"{results}",
			},
			"contains_restricted_tags":
				"__`       `__ | ⚠🚫 | 制限付きタグが含まれています。",
			"start_interactive":
				"インタラクティブを開始"
		},

		"results_browser": { # Over half of what would be here actually uses the doujin_info material
			"buttons": {
				"select":
					"番号付きのボタンを使用して結果番号を入力してください。\n"
					"[◀=バックスペース][🗑=キャンセル][✅=入力]",
				"read_later_full":
					"❌ 後で読むリストがいっぱいです。 このアクションを実行するには、そこから何かを削除してください。",
				"add_to_read_later":
					"✅ 後で読むリストに `{code}` を追加しました。",
				"remove_from_read_later":
					"✅ 後で読むリストから `{code}` を削除しました。",
				"support_server":
					"サポートサーバー"
			},
			"forbidden": {
				"title":
					"禁断",
				"description":
					"⚠️❌ この成人雜誌はこのサーバーでは表示できません。"
			},
			"minimal_details": 
				"最小限の詳細"
		},
	},

	"cn": {
		"language_not_available": {
			"description": 
				"此命令在您的语言中不可用。 你要继续吗？",
			"footer":
				"您可以通過訪問支持公會來幫助翻譯 NReader。",
			"button": 
				"继续"
		},
		"language_options": {
			"english": 
				"英語",
			"japanese":
				"日語",
			"chinese":
				"中文"
		},

		"notifications_due": {
			"first_time_tip": {
				"title":
					"首次互動通知",
				"description":
					"👋 看來你是第一次使用這個機器人！\n"
					"🔞 此機器人僅供成人使用，只能在 NSFW 頻道中使用。\n"
					"ℹ️ 如需更多信息，請使用 「`n!help`」 命令。\n"
					"ℹ️ 有關法律信息，請使用 「`n!legal`」 命令。\n"
					"ℹ️ MechHub 強烈推薦您加入支持公會：**[MechHub/DJ4wdsRYy2](https://discord.gg/DJ4wdsRYy2)**\n"
			},

			"lolicon_viewing_tip": 
				"提示：要在 Discord 上查看受限制的漫畫，您需要邀請我加入您擁有的服務器並運行 「`n!whitelist <'add' or'remove'>`」 命令。\n"
				"這將允許您服務器上的所有用戶打開受限的成人雜誌圈。\n"
				"受限制的成人雜誌__僅__反映在您在**白名單服務器**上的歷史記錄、收藏夾、書籤或搜索中，但統計數據**可能不會**從這些域中隱藏此內容。"
		},

		"help": {
			"title": 
				"<:info:818664266390700074> 幫助",
			"description": 
				"**在 Discord 中搜索、概覽和閱讀成人雜誌。**\n" 
				"**支持公會: [MechHub/DJ4wdsRYy2](https://discord.gg/DJ4wdsRYy2)**\n" 
				"\n" 
				"如需完整信息表，請訪問 [此 Google 文檔頁面](https://docs.google.com/document/d/e/2PACX-1vTszuOx36UbKmAhyX2sQ4jEJymmkyzf6oz-JduErnFxbWhoXoHeFEd0ZPv-VnKiUMFV4a_H8WjU1iPE/pub)。\n"
				"\n"
				"更改機器人語言也將重置首次通知。",
			"footer": 
				"由 MechHub 提供"
		},

		"invite": {
			"title": 
				"邀請 NReader",
			"description": 
				"[點擊這裡]({url})邀請這個機器人加入你的公會。",
			"footer": 
				"由 MechHub 提供"
		},

		"doujin_info": {
			"sfw": {
				"顯示最少的信息。 在 NSFW 標記的頻道中使用該命令以獲取更多詳細信息。"
			},
			"not_a_valid_id": 
				"❌ 標識無效。 只有數字！",
			"doujin_not_found": 
				"🔎❌ 那個漫畫不存在。",
			"is_lolicon":
				"⚠️⛔ 這本漫畫包含不允許的標籤。",
			"fields": {
				"not_provided":
					"無法使用",
				"original":
					"原來的",

				"title": 
					"標題",

				"id/pages":
					"鑑別 || 頁",

				"date_uploaded":
					"上傳日期",
				"date_uploaded_weekdays": {
					0: "星期日", 1: "星期一", 2: "星期二", 3: "星期三",
					4: "星期四", 5: "星期五", 6: "星期六"
				},

				"languages":
					"成人雜誌語言",
				"language_names": {
					"translated": "已翻譯",
					"rewrite": "又寫了",
					"speechless": "沒有對話",
					"text cleaned": "文字已刪除 ",
					"japanese": "日語",
					"english": "英語",
					"chinese": "中文",
					"cebuano": "宿務語",
					"arabic": "阿拉伯語",
					"javanese": "爪哇語"
				},

				"artists":
					"成人雜誌藝人",

				"characters":
					"成人雜誌角色",

				"parodies":
					"成人雜誌模仿",

				"tags": 
					"內容標籤",
				"tag_names": {},  # Translate a bunch of different common tags
			},
			
			"read": 
				"讀",
			"expand_thumbnail":
				"展開圖片",
			"minimize_thumbnail":
				"最小化圖像",
			"need_permissions":
				"需要許可",
			"unexpected_loss":
				"❌ 所需的權限意外丟失。",
			"opened":
				"打開"
		},

		"page_reader": { 
			"description": {
				"previous":
					"以前的",
				"next": 
					"下一個",
				"finish":
					"**結束**",
				"select":
					"選擇",
				"stop":
					"停止",
				"pause":
					"暫停",
				"bookmark":
					"書籤",
				"unbookmark":
					"取消書籤"
			},

			"footer": 
				"頁面 [{current}/{total}] {bookmark}",
			"redirect_button":
				"支援公会",

			"init": {
				"description":
					"等待。",
				"footer":
					"頁面 [0/{total}]：按 ▶ 開始開始閱讀。",
				"button":
					"開始",
			},

			"portal":
				"單擊/點按上面提到的內容可跳轉到您的閱讀器。\n"
				"你打開了`{code}`：`{name}`",
			"closing":
				"關閉...",
			"timeout":
				"您在頁面 [{current}/{total}] 上超時。",
			"timeout_notification":
				"{mention}, 您在閱讀器中超時。忘記按暫停？",
			"finished":
				"你完成了這本漫畫。",
			"select_inquiry": {
				"description":
					"使用編號按鈕輸入頁碼\n"
					"[◀ = 退格] [🗑 = 取消] [✅ = 回車] [🔖 = 書籤]",
				"footer":
					"書籤頁面：{bookmarked_page}",
			},
			"paused":
				"你暫停了這本漫畫。",
			"recall_saved": {
				"title":
					"召回已保存。",
				"description": 
					"保存了代碼「`{code}`」的漫畫，以回憶頁面 [{current}/{total}]。\n"
					"要返回此頁面，請運行「`n!recall`」命令以立即打開從該頁面開始的新閱讀器。",
			},
			"stopped":
				"你已經停止閱讀這本漫畫了。",
			"cannot_bookmark_first_page":
				"您不能為第一頁添加書籤。請改用收藏夾！",
			"bookmarks_full":
				"❌ 您的書籤列表已滿。請從中刪除某些內容以執行此操作。",
			"favorites_full":
				"❌ 您的收藏夾列表已滿。請從中刪除某些內容以執行此操作。",
			"added_to_favorites":
				"✅ 將「`{code}`」添加到您的收藏夾。",
			"removed_from_favorites":
				"✅ 您的收藏夾中刪除了「`{code}`」。",
			"error":
				"發生未處理的錯誤；請重試。\n"
				"如果問題仍然存在，請嘗試重新打開漫畫。\n"
				"如果重新打開不起作用，請單擊「支持公會」按鈕。"
		},

		
		"search_doujins": {  
			"searching": 
				"<a:nreader_loading:810936543401213953> 搜索...\n"
				"```\n"
				"{query} {appendage}\n"
				"```\n",

			"invalid_page": {
				"title":
					"❌ 頁碼無效。",
				"description":
					"`0` (零) 不是有效的頁碼。 頁碼必須大於零。"
			},
			"invalid_sort": {
				"title":
					"❌ 無效的排序參數。",
				"description":
					"我只能按 `today`、`week`、`month`、`popular`（默認）、和 `recent` 排序。"
			},
			"too_broad": {
				"title":
					"❌ 搜索範圍太廣。",
				"description":
					"告訴我要搜索什麼，或者檢查你的搜索附件（參見 `n!help` 下的 `search_appendage`）。"
			},
			"unexpected_error":
				"❌ 意外的錯誤。 請嘗試其他搜索。",
			"no_results": {
				"title":
					"🔎❌ 沒有結果。",
				"description": {
					"appendage": 
						"`*️⃣` 這可能是您的搜索附件的原因。 請參閱 `n!help` 下的 `search_appendage`，或添加 `--noappend` 以繞過它。",
					"page":
						"`*️⃣` 您已在搜索中添加頁碼 (`--page=#`)。 請檢查您的頁面是否在總頁數範圍內（通過不搜索頁面進行檢查）。",
					"restricted_tags":
						"`*️⃣` 您搜索了受限標籤。 由於此機器人的工作方式，受限標籤會被取消，從而導致空搜索。"
				}
			},

			"search_results": {
				"title":
					"搜索結果",
				"description":
					"顯示第 {page}/{pages} 頁（~{approximate} 漫畫）：\n"
					"{results}",
			},
			"contains_restricted_tags":
				"__`       `__ | ⚠🚫 | 包含受限標籤。",
			"start_interactive":
				"開始互動"
		},

		"results_browser": { # Over half of what would be here actually uses the doujin_info material
			"buttons": {
				"select":
					"使用編號按鈕輸入結果編號。\n"
					"[◀ = 退格] [🗑 = 取消] [✅ = 回車]",
				"read_later_full":
					"❌ 您的稍後閱讀列表已滿。 請從中刪除某些內容以執行此操作。",
				"add_to_read_later":
					"✅ 將 `{code}` 添加到您的稍後閱讀列表中。",
				"remove_from_read_later":
					"✅ 從您的稍後閱讀列表中刪除了 `{code}`。",
				"support_server":
					"支持服務器"
			},
			"forbidden": {
				"title":
					"禁止的",
				"description":
					"⚠️❌ 此成人雜誌無法在此服務器中查看。"
			},
			"minimal_details": 
				"最少的細節"
		},
	}
}

from discord.ext.commands.cog import Cog

class Localization(Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Localization(bot))