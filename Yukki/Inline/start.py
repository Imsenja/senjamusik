from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="π Kualitas Suara", callback_data="AQ"),
            InlineKeyboardButton(text="π Volume Suara", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Auth Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="β Tutup", callback_data="close"),
        ],
    ]
    return f"βοΈ  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="βοΈ Pengaturan", callback_data="settingm"
                )
            ],
        ]
        return f"π  **Ini Adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="βοΈ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π₯Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini Adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="βοΈ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="β‘Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **Ini Adalah {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="βοΈ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="β‘Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="β‘Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini Adalah {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"π  **Ini Adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="β‘Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini Adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="β‘Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="β‘Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="β‘Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini Adalah {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="π Kualitas Suara", callback_data="AQ"),
            InlineKeyboardButton(text="π Volume Suara", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Auth Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="βοΈ Tutup", callback_data="close"),
            InlineKeyboardButton(text="π Kembali", callback_data="okaybhai"),
        ],
    ]
    return f"βοΈ  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="π Reset Volume Audio π", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="π Vol Rendah", callback_data="LV"),
            InlineKeyboardButton(text="π Vol Medium", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="π Vol Tinggi", callback_data="HV"),
            InlineKeyboardButton(text="π Vol Diperkuat", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="π½ Custom Volume π½", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="π Kembali", callback_data="settingm")],
    ]
    return f"βοΈ  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="πΌCustom Volume πΌ", callback_data="AV")],
    ]
    return f"βοΈ  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="π₯ Semua", callback_data="EVE"),
            InlineKeyboardButton(text="π€΄ Admin", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="π List Pengguna Auth", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="π Kembali", callback_data="settingm")],
    ]
    return f"βοΈ  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="βοΈ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="πΎ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="π» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="π½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="π Go back", callback_data="settingm")],
    ]
    return f"βοΈ  **{MUSIC_BOT_NAME} Pengaturan**", buttons
