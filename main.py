"""MagicLeague Core File

Moving legacy code to GitHub for future maintenance. Originally written in 2018.
"""

print("Loading...")

import logging
import shlex
import sqlite3

import discord
from fuzzywuzzy import process

__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "CC0"
__version__ = "5.6.2022"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"

logging.basicConfig(level=logging.INFO)

client = discord.Client()
configDb = sqlite3.connect("/usr/src/db/config.db")
configDb.text_factory = str


@client.event
async def on_ready():
    startup = logging.getLogger("startup")
    startup.info("===MagicLeague 2 is now starting up!===")
    startup.info('USERNAME: {0.user}'.format(client))
    startup.info('ID: {0.user.id}'.format(client))
    startup.info("SERVERS: " + str(sum(1 for x in client.guilds)))

    dbCheck = configDb.cursor()
    dbCheck.execute("SELECT count(*) FROM sqlite_master WHERE type='table' and name='config'")
    if dbCheck.fetchone()[0] == 1:
        dbCheck.close()
    else:
        startup.warning("Config table not found! Creating new table.")
        dbCheck.execute("CREATE TABLE config(id TEXT, name TEXT, value TEXT)")
        configDb.commit()
        dbCheck.close()
        startup.warning("Config table has been created.")


###cfgCommandPrefix###
async def cfgGet_CommandPrefix(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgcommandprefix' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("m^")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_CommandPrefix(guild, prefix):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), prefix)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgcommandprefix'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgcommandprefix', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgRoleFreeAgent###
async def cfgGet_RoleFreeAgent(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgrolefreeagent' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_RoleFreeAgent(guild, roleids):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), roleids)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgrolefreeagent'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgrolefreeagent', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgRoleTeamStaff###
async def cfgGet_RoleTeamStaff(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleteamstaff' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_RoleTeamStaff(guild, roleids):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), roleids)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleteamstaff'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleteamstaff', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgRoleTeamOwner###
async def cfgGet_RoleTeamOwner(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleteamowner' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_RoleTeamOwner(guild, roleids):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), roleids)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleteamowner'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleteamowner', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgRoleServerStaff###
async def cfgGet_RoleServerStaff(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleserverstaff' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_RoleServerStaff(guild, roleids):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), roleids)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleserverstaff'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleserverstaff', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgRoleServerOwner###
async def cfgGet_RoleServerOwner(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleserverowner' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_RoleServerOwner(guild, roleids):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), roleids)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleserverowner'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleserverowner', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgChannelTransactionsID###
async def cfgGet_ChannelTransactionsID(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgchanneltransactionsid' LIMIT 1",
                       payload)))[3:-4]
    if not o:
        cfgGet.close()
        return ("")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_ChannelTransactionsID(guild, channelids):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), channelids)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgchanneltransactionsid'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgchanneltransactionsid', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgChannelTransactionsToggle###
async def cfgGet_ChannelTransactionsToggle(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(
        cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgchanneltransactionstoggle' LIMIT 1",
                       payload)))[3:-4]
    if not o:
        cfgGet.close()
        return ("false")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_ChannelTransactionsToggle(guild, toggle):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), toggle)
    purge = (str(guild.id),)
    # cfgSet.execute("DELETE FROM config WHERE EXISTS (SELECT * FROM config WHERE id = ? AND name = 'cfgchanneltransactionstoggle')", purge)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgchanneltransactionstoggle'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgchanneltransactionstoggle', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgTransactionsToggle###
async def cfgGet_TransactionsToggle(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgtransactionstoggle' LIMIT 1",
                                payload)))[3:-4]
    if not o:
        cfgGet.close()
        return ("true")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_TransactionsToggle(guild, toggle):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), toggle)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgtransactionstoggle'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgtransactionstoggle', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgTextRelease###
async def cfgGet_TextRelease(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(
        list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgtextrelease' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("%playermention% has been released from %teammention%!")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_TextRelease(guild, text):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), text)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgtextrelease'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgtextrelease', ?)", payload)
    configDb.commit()
    cfgSet.close()


###
###cfgTextSign###
async def cfgGet_TextSign(guild):
    cfgGet = configDb.cursor()
    payload = (str(guild.id),)
    o = str(
        list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgtextsign' LIMIT 1", payload)))[
        3:-4]
    if not o:
        cfgGet.close()
        return ("%playermention% has been signed to %teammention%")  # default value
    else:
        cfgGet.close()
        return (o)


async def cfgSet_TextSign(guild, text):
    cfgSet = configDb.cursor()
    payload = (str(guild.id), text)
    purge = (str(guild.id),)
    cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgtextsign'", purge)
    cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgtextsign', ?)", payload)
    configDb.commit()
    cfgSet.close()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    debug_log = logging.getLogger("debug")

    msgPrefix = await cfgGet_CommandPrefix(message.guild)

    if message.content.startswith(msgPrefix) or message.content.startswith("m^"):
        if message.content.startswith("m^"):
            content = message.clean_content.replace("m^", "", 1).strip()
        else:
            content = message.clean_content.replace(msgPrefix, "", 1).strip()
        role_mentions = message.role_mentions
        channel_mentions = message.channel_mentions
        member_mentions = message.mentions
        try:
            command = content.split()[0].lower()
        except IndexError:
            command = "null"  # Sets command to null to trigger unknown
            content = (content + "null")  # Adds null to content to bypass del flags.
            pass
        flags = content.lower().split()  # array of input flags all lowercase.
        del flags[0]
        flagsOriginal = content.split()  # array of input flags original formatting.
        del flagsOriginal[0]
        flagsLexical = shlex.split(message.content.replace("m^", "", 1).strip())
        del flagsLexical[0]
        logger = logging.getLogger(message.guild.name)

        # Outputs into log when a command has been run.
        logger.info(message.author.name + ":" + content)

        if command == "config":
            try:
                flags[0]
            except IndexError:
                await message.channel.send("ERROR: Missing flag: Config Mode")
                pass
            else:

                if flags[0] == "set":

                    # Checks if user is server owner.
                    owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
                    if [i for i in [str(role.id) for role in message.author.roles] if
                        i in owners] or message.channel.permissions_for(message.author).administrator:

                        # Checks if a config name has been provided.
                        try:
                            flags[1]
                        except IndexError:
                            await message.channel.send("ERROR: Missing flag: Config Name")
                            pass
                        else:

                            if (flags[1] == "cfgcommandprefix") or (flags[1] == "cfgcp"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: PREFIX")
                                    pass
                                else:
                                    await cfgSet_CommandPrefix(message.guild, flags[2])
                                    await message.channel.send(
                                        "cfgCommandPrefix updated. Verified value: " + await cfgGet_CommandPrefix(
                                            message.guild))

                            elif (flags[1] == "cfgtransactionstoggle") or (flags[1] == "cfgtt"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: BOOLEAN")
                                    pass
                                else:
                                    if flags[2] == "true":
                                        await cfgSet_TransactionsToggle(message.guild, flags[2])
                                        await message.channel.send(
                                            "cfgTransactionsToggle updated. Verified value: " + await cfgGet_TransactionsToggle(
                                                message.guild))
                                    elif flags[2] == "false":
                                        await cfgSet_TransactionsToggle(message.guild, flags[2])
                                        await message.channel.send(
                                            "cfgTransactionsToggle updated. Verified value: " + await cfgGet_TransactionsToggle(
                                                message.guild))
                                    else:
                                        await message.channel.send("ERROR: Invalid flag: Must be true/false!")

                            elif (flags[1] == "cfgrolefreeagent") or (flags[1] == "cfgrfa"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleFreeAgent(message.guild, pl)
                                        await message.channel.send(
                                            "cfgRoleFreeAgent updated. Verified value: " + await cfgGet_RoleFreeAgent(
                                                message.guild))

                            elif (flags[1] == "cfgroleteamstaff") or (flags[1] == "cfgrts"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleTeamStaff(message.guild, pl)
                                        await message.channel.send(
                                            "cfgRoleTeamStaff updated. Verified value: " + await cfgGet_RoleTeamStaff(
                                                message.guild))

                            elif (flags[1] == "cfgroleteamowner") or (flags[1] == "cfgrto"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleTeamOwner(message.guild, pl)
                                        await message.channel.send(
                                            "cfgRoleTeamOwner updated. Verified value: " + await cfgGet_RoleTeamOwner(
                                                message.guild))

                            elif (flags[1] == "cfgroleserverstaff") or (flags[1] == "cfgrss"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleServerStaff(message.guild, pl)
                                        await message.channel.send(
                                            "cfgRoleServerStaff updated. Verified value: " + await cfgGet_RoleServerStaff(
                                                message.guild))

                            elif (flags[1] == "cfgroleserverowner") or (flags[1] == "cfgrso"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleServerOwner(message.guild, pl)
                                        await message.channel.send(
                                            "cfgRoleServerOwner updated. Verified value: " + await cfgGet_RoleServerOwner(
                                                message.guild))

                            elif (flags[1] == "cfgchanneltransactionsid") or (flags[1] == "cfgctid"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        channel_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Channel Mentions")
                                    else:
                                        pl = ""
                                        for channel in channel_mentions:
                                            pl = pl + str(channel.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_ChannelTransactionsID(message.guild, pl)
                                        await message.channel.send(
                                            "cfgChannelTransactionsID updated. Verified value: " + await cfgGet_ChannelTransactionsID(
                                                message.guild))

                            elif (flags[1] == "cfgchanneltransactionstoggle") or (flags[1] == "cfgctt"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: BOOLEAN")
                                    pass
                                else:
                                    if flags[2] == "true":
                                        await cfgSet_ChannelTransactionsToggle(message.guild, flags[2])
                                        await message.channel.send(
                                            "cfgChannelTransactionsToggle updated. Verified value: " + await cfgGet_ChannelTransactionsToggle(
                                                message.guild))
                                    elif flags[2] == "false":
                                        await cfgSet_ChannelTransactionsToggle(message.guild, flags[2])
                                        await message.channel.send(
                                            "cfgChannelTransactionsToggle updated. Verified value: " + await cfgGet_ChannelTransactionsToggle(
                                                message.guild))
                                    else:
                                        await message.channel.send("ERROR: Invalid flag: Must be true/false!")

                            elif (flags[1] == "cfgtextrelease") or (flags[1] == "cfgtr"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: STRING")
                                    pass
                                else:
                                    pl = flagsOriginal[2:]
                                    plStr = ' '.join(pl)
                                    await cfgSet_TextRelease(message.guild, plStr)
                                    await message.channel.send(
                                        "cfgTextRelease updated. Verified value: " + await cfgGet_TextRelease(
                                            message.guild))

                            elif (flags[1] == "cfgtextsign") or (flags[1] == "cfgts"):
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: STRING")
                                    pass
                                else:
                                    pl = flagsOriginal[2:]
                                    plStr = ' '.join(pl)
                                    await cfgSet_TextSign(message.guild, plStr)
                                    await message.channel.send(
                                        "cfgTextSign updated. Verified value: " + await cfgGet_TextSign(message.guild))

                            else:
                                await message.channel.send("ERROR: Invalid flag: Config Name")

                    else:
                        await message.channel.send("ERROR: Config Error: You are not server owner.")

                elif flags[0] == "list":
                    # Returns all of the configs and their settings.
                    msgGuild = message.guild
                    pl = "`config set > `\n" \
                         "    `cfgCommandPrefix/cfgCP:` " + await cfgGet_CommandPrefix(msgGuild) + "\n" \
                                                                                                   "    `cfgRoleFreeAgent/cfgRFA:` " + await cfgGet_RoleFreeAgent(
                        msgGuild) + "\n" \
                                    "    `cfgRoleTeamStaff/cfgRTS:` " + await cfgGet_RoleTeamStaff(msgGuild) + "\n" \
                                                                                                               "    `cfgRoleTeamOwner/cfgRTO:` " + await cfgGet_RoleTeamOwner(
                        msgGuild) + "\n" \
                                    "    `cfgRoleServerStaff/cfgRSS:` " + await cfgGet_RoleServerStaff(msgGuild) + "\n" \
                                                                                                                   "    `cfgRoleServerOwner/cfgRSO:` " + await cfgGet_RoleServerOwner(
                        msgGuild) + "\n" \
                                    "    `cfgChannelTransactionsID/cfgCTID:` " + await cfgGet_ChannelTransactionsID(
                        msgGuild) + "\n" \
                                    "    `cfgChannelTransactionsToggle/cfgCTT:` " + await cfgGet_ChannelTransactionsToggle(
                        msgGuild) + "\n" \
                                    "    `cfgTransactionsToggle/cfgTT:` " + await cfgGet_TransactionsToggle(
                        msgGuild) + "\n" \
                                    "    `cfgTextRelease/cfgTR:` " + await cfgGet_TextRelease(msgGuild) + "\n" \
                                                                                                          "    `cfgTextSign/cfgTS:` " + await cfgGet_TextSign(
                        msgGuild) + "\n"
                    await message.channel.send(pl)
                else:
                    # If provided flag is invalid.
                    await message.channel.send("ERROR: Invalid flag: Config Mode")

        elif command == "getid":
            # GetID will return the Discord ID of anything mentioned. Role, channel, or member.
            pl = ""
            for role in role_mentions:
                pl = pl + "`Role: `" + role.name + " id: " + str(role.id) + "\n"
            for channel in channel_mentions:
                pl = pl + "`Channel: `" + channel.name + " id: " + str(channel.id) + "\n"
            for member in member_mentions:
                pl = pl + "`Member: `" + member.name + " id : " + str(member.id) + "\n"
            try:
                await message.channel.send(pl)
            except discord.errors.HTTPException:
                await message.channel.send("ERROR: Must mention a role, channel, or member!")

        elif command == "debug":
            await message.channel.send(f"Flags: {str(flagsLexical)}")

        elif command == "sign":
            # Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',')

            # Check if signing is enabled or valid override
            if await cfgGet_TransactionsToggle(message.guild) == "true" or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                # Gets the channel ID of the contract channel
                contract_channel = str(await cfgGet_ChannelTransactionsID(message.guild)).split(',')

                # Checks if message is in contract channel, or the contract channel is disabled. Overrides if staff or owner.
                if (await cfgGet_ChannelTransactionsToggle(message.guild) == "true" and str(
                        message.channel.id) in contract_channel) or \
                        await cfgGet_ChannelTransactionsToggle(message.guild) == "false" or \
                        [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                        [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                    # Ensure one member has been mentioned
                    try:
                        member_mentions[0]
                    except IndexError:
                        await message.channel.send("ERROR: Sign Error: You must mention a member!")
                    else:

                        # FuzzyWuzzy Patch-in Support Code
                        found_role = None
                        # Ensure one role has been mentioned
                        try:
                            role_mentions[0]
                        except IndexError:
                            found_name = process.extractOne(flagsLexical[1],
                                                            [role.name for role in message.guild.roles])
                            found_role = discord.utils.find(lambda m: m.name == found_name[0], message.guild.roles)
                            if found_role is None:
                                await message.channel.send("ERROR: Sign Error: You must mention a role!")
                                return
                        else:
                            found_role = role_mentions[0]
                        # Get required configs for the server
                        team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
                        team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')
                        free_agent = str(await cfgGet_RoleFreeAgent(message.guild)).split(',')

                        # Bugfix 5/6/2022: Ensure the role being released from is not a server role.
                        if str(found_role.id) in owners + server_staff + team_owners + team_staff + free_agent:
                            await message.channel.send("ERROR: The mentioned role does not appear to be a team.")
                            return

                        # Checks if user is owner, server staff, team owner, or team staff.
                        if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                                ([i for i in [str(role.id) for role in message.author.roles] if
                                  i in team_owners] and found_role in message.author.roles) or \
                                ([i for i in [str(role.id) for role in message.author.roles] if
                                  i in team_staff] and found_role in message.author.roles):

                            # Checks if mentioned user is a free agent.
                            if [i for i in [str(role.id) for role in member_mentions[0].roles] if i in free_agent]:

                                # Removes all roles that are in the Free Agent role list.
                                for role in member_mentions[0].roles:
                                    if str(role.id) in free_agent:
                                        # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                        # Patch 5/6/2022: Added permission checking.
                                        try:
                                            await member_mentions[0].remove_roles(role)
                                        except discord.errors.Forbidden:
                                            await message.channel.send("Unable to remove the free agent role! Please check your permissions.")
                                            return

                                # Adds the mentioned role to the user.
                                # while found_role not in member_mentions[0].roles:
                                # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                # Patch 5/6/2022: Added restore state if adding role fails.
                                try:
                                    await member_mentions[0].add_roles(found_role)
                                except discord.errors.Forbidden:
                                    await message.channel.send("Unable to add the tagged role! Please check your permissions. Restoring free agent roles.")
                                    for roleID in free_agent:
                                        free_agent_role = discord.utils.find(lambda f: f.id == int(roleID),
                                                                             message.guild.roles)
                                        # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                        # while free_agent_role not in member_mentions[0].roles:

                                        # Checks if the bot can assign the role, and ignores an exception if it can't.
                                        try:
                                            await member_mentions[0].add_roles(free_agent_role)
                                        except discord.errors.Forbidden:
                                            await message.channel.send(
                                                "ERROR: Release Error: Unable to assign the following role: " + free_agent_role.mention + "\nPlease check your free agent settings!")
                                            return

                                # Grabs the sign text and sends it. Replaces tags where needed.
                                await message.channel.send(
                                    str(await cfgGet_TextSign(message.guild)).replace("%playermention%",
                                                                                      member_mentions[
                                                                                          0].mention).replace(
                                        "%teammention%", found_role.mention).replace("%playername%",
                                                                                     member_mentions[0].name).replace(
                                        "%teamname%", found_role.name))

                            else:
                                await message.channel.send("ERROR: Sign Error: That user is not a valid free agent!")
                        else:
                            await message.channel.send(
                                "ERROR: Sign Error: You do not have permission to sign to this team!")
                else:
                    await message.channel.send("ERROR: Sign Error: You must sign within the contract channel!")
            else:
                await message.channel.send("ERROR: Sign Error: Transactions are currently disabled!")

        elif command == "release":
            # Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',')

            # Check if signing is enabled or valid override
            if await cfgGet_TransactionsToggle(message.guild) == "true" or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                # Gets the channel ID of the contract channel as well as owners
                contract_channel = str(await cfgGet_ChannelTransactionsID(message.guild)).split(',')

                # Checks if message is in contract channel, or the contract channel is disabled. Overrides if staff or owner.
                if (await cfgGet_ChannelTransactionsToggle(message.guild) == "true" and str(
                        message.channel.id) in contract_channel) or \
                        await cfgGet_ChannelTransactionsToggle(message.guild) == "false" or \
                        [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                        [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                    # Ensure one member has been mentioned
                    try:
                        member_mentions[0]
                    except IndexError:
                        await message.channel.send("ERROR: Release Error: You must mention a member!")
                    else:

                        # FuzzyWuzzy Patch-in Support Code
                        found_role = None
                        # Ensure one role has been mentioned
                        try:
                            role_mentions[0]
                        except IndexError:
                            found_name = process.extractOne(flagsLexical[1],
                                                            [role.name for role in message.guild.roles])
                            found_role = discord.utils.find(lambda m: m.name == found_name[0], message.guild.roles)
                            if found_role is None:
                                await message.channel.send("ERROR: Release Error: You must mention a role!")
                                return
                        else:
                            found_role = role_mentions[0]
                        # Get required configs for the server
                        team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
                        team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')
                        free_agent = str(await cfgGet_RoleFreeAgent(message.guild)).split(',')

                        # Bugfix 5/6/2022: Ensure the role being released from is not a server role.
                        if str(found_role.id) in owners + server_staff + team_owners + team_staff + free_agent:
                            await message.channel.send("ERROR: The mentioned role does not appear to be a team.")
                            return

                        # Checks if user is owner, server staff, team owner, or team staff.
                        if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                                ([i for i in [str(role.id) for role in message.author.roles] if
                                  i in team_owners] and found_role in message.author.roles) or \
                                ([i for i in [str(role.id) for role in message.author.roles] if
                                  i in team_staff] and found_role in message.author.roles):

                            # Checks if mentioned user is on mentioned team.
                            if str(found_role.id) in [str(role.id) for role in member_mentions[0].roles]:

                                # Checks if user is currently staff
                                if [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_staff]:
                                    await message.channel.send(
                                        "ERROR: Release Error: That user is a team staff. Demote them before releasing them.")

                                elif [i for i in [str(role.id) for role in member_mentions[0].roles] if
                                      i in team_owners]:
                                    await message.channel.send(
                                        "ERROR: Release Error: That user is a team owner. Demote them before releasing them.")
                                else:
                                    # Removes mentioned role.
                                    # while found_role in member_mentions[0].roles:
                                    # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                    # Patch 5/6/2022: Added permission check for removing roles.
                                    try:
                                        await member_mentions[0].remove_roles(found_role)
                                    except discord.errors.Forbidden:
                                        await message.channel.send("ERROR: Unable to remove tagged role from user, please check your permission settings!")
                                        return

                                    # Adds free agent role.
                                    for roleID in free_agent:
                                        free_agent_role = discord.utils.find(lambda f: f.id == int(roleID),
                                                                             message.guild.roles)
                                        # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                        # while free_agent_role not in member_mentions[0].roles:

                                        # Checks if the bot can assign the role, and ignores an exception if it can't.
                                        try:
                                            await member_mentions[0].add_roles(free_agent_role)
                                        except discord.errors.Forbidden:
                                            await message.channel.send(
                                                "ERROR: Release Error: Unable to assign the following role: " + free_agent_role.mention + "\nPlease check your free agent settings!")
                                            pass

                                    # Grabs the sign text and sends it. Replaces tags where needed.
                                    await message.channel.send(
                                        str(await cfgGet_TextRelease(message.guild)).replace("%playermention%",
                                                                                             member_mentions[
                                                                                                 0].mention).replace(
                                            "%teammention%", found_role.mention).replace("%playername%",
                                                                                         member_mentions[
                                                                                             0].name).replace(
                                            "%teamname%", found_role.name))

                            else:
                                await message.channel.send("ERROR: Release Error: That user is not on that team!")
                        else:
                            await message.channel.send(
                                "ERROR: Release Error: You do not have permission to sign to this team!")
                else:
                    await message.channel.send("ERROR: Release Error: You must sign within the contract channel!")
            else:
                await message.channel.send("ERROR: Release Error: Transactions are currently disabled!")

        elif command == "promote":
            # Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',')

            # Grabs team owners and team staff for authentication
            team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
            team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')

            # Checks if message author is either an owner, server staff, or team owner.
            if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in team_owners]:

                # Checks if a member was mentioned.
                try:
                    member_mentions[0]
                except IndexError:
                    await message.channel.send("ERROR: Promote Error: You must mention a member!")
                else:

                    # Checks if a team and staff role was mentioned.
                    try:
                        role_mentions[0]
                        role_mentions[1]
                    except IndexError:
                        await message.channel.send(
                            "ERROR: Promote Error: You must mention two roles! One team and a staff role.")
                    else:

                        # Figures out which role mentioned is the staff role.
                        if (str(role_mentions[0].id) in team_staff or str(role_mentions[0].id) in team_owners) and str(
                                role_mentions[1].id) not in team_staff:
                            staff_role = role_mentions[0]
                            team_role = role_mentions[1]
                        elif (str(role_mentions[1].id) in team_staff or str(
                                role_mentions[1].id) in team_owners) and str(role_mentions[0].id) not in team_staff:
                            staff_role = role_mentions[1]
                            team_role = role_mentions[0]
                        else:
                            await message.channel.send(
                                "ERROR: Promote Error: It seems that both roles you've mentioned are staff roles or team roles.")
                            return

                        # If staff_role has been set, continue
                        if staff_role:

                            # Checks if staff role is team owner.
                            if str(staff_role.id) in team_owners:

                                # Checks that user is server staff before assigning team owner role.
                                if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                        [i for i in [str(role.id) for role in message.author.roles] if
                                         i in server_staff]:

                                    # while staff_role not in member_mentions[0].roles:
                                    # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                    try:
                                        await member_mentions[0].add_roles(staff_role)
                                    except discord.errors.Forbidden:
                                        await message.channel.send(
                                            "ERROR: Promote Error: Unable to assign the staff role! Check permissions.")
                                        pass
                                    else:
                                        await message.channel.send(
                                            member_mentions[0].mention + " has been promoted to " + staff_role.mention)

                                else:
                                    await message.channel.send(
                                        "ERROR: Promote Error: Only server staff can promote to team owner!")

                            else:
                                # Checks if user is on the team
                                if team_role in member_mentions[0].roles:

                                    # Checks if user is not already staff:
                                    if not [i for i in [str(role.id) for role in member_mentions[0].roles] if
                                            i in team_staff]:

                                        # Checks that message author is on the mentioned team. Verifies override.
                                        if team_role in message.author.roles or \
                                                [i for i in [str(role.id) for role in message.author.roles] if
                                                 i in owners] or \
                                                [i for i in [str(role.id) for role in message.author.roles] if
                                                 i in server_staff]:

                                            # Assigns staff role.
                                            # while staff_role not in member_mentions[0].roles:
                                            # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                            try:
                                                await member_mentions[0].add_roles(staff_role)
                                            except discord.errors.Forbidden:
                                                await message.channel.send(
                                                    "ERROR: Promote Error: Unable to assign the staff role! Check permissions.")
                                                pass
                                            else:
                                                await message.channel.send(member_mentions[
                                                                               0].mention + " has been promoted to " + staff_role.mention)
                                        else:
                                            await message.channel.send(
                                                "ERROR: Promote Error: It seems you are not the owner of that team!")

                                    else:
                                        await message.channel.send(
                                            "ERROR: Promote Error: That user is already a staff member!")

                                else:
                                    await message.channel.send(
                                        "ERROR: Promote Error: That user is not on the mentioned team!")

            else:
                await message.channel.send("ERROR: Promote Error: You do not have the required roles to promote!")

        elif command == "demote":
            # Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',')

            # Grabs team owners and team staff for authentication
            team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
            team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')

            # Checks if message author is either an owner, server staff, or team owner.
            if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in team_owners]:

                # Checks if a member was mentioned.
                try:
                    member_mentions[0]
                except IndexError:
                    await message.channel.send("ERROR: Demote Error: You must mention a member!")
                else:

                    # Checks if a team was mentioned. A staff role does not need to be mentioned here.
                    try:
                        role_mentions[0]
                    except IndexError:
                        await message.channel.send("ERROR: Demote Error: You must mention a team!")
                    else:

                        # Checks if user is on team
                        if role_mentions[0] in member_mentions[0].roles:

                            # Checks if user is staff.
                            if [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_staff]:

                                # Checks if author is a team owner. Checks override.
                                if role_mentions[0] in message.author.roles or \
                                        [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                        [i for i in [str(role.id) for role in message.author.roles] if
                                         i in server_staff]:

                                    # Removes staff role.
                                    for role in member_mentions[0].roles:
                                        if str(role.id) in team_staff:
                                            # while role in member_mentions[0].roles:
                                            # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                            try:
                                                await member_mentions[0].remove_roles(role)
                                            except discord.errors.Forbidden:
                                                await message.channel.send(
                                                    "ERROR: Demote Error: Unable to remove the staff role! Check permissions.")
                                                break
                                            else:
                                                await message.channel.send(member_mentions[
                                                                               0].mention + " has been demoted from " + role.mention)

                                else:
                                    await message.channel.send(
                                        "Error: Demote Error: You are not on that team.\n`Tip: Do not mention the role you are demoting from!`")

                            # If user is not staff, check if they are team owners.
                            elif [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_owners]:

                                # Checks if author is server staff or server owner.
                                if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                        [i for i in [str(role.id) for role in message.author.roles] if
                                         i in server_staff]:

                                    # Removes team owner role.
                                    for role in member_mentions[0].roles:
                                        if str(role.id) in team_owners:
                                            # while role in member_mentions[0].roles:
                                            # Patch 4/20/2021: Removed the check loops. They were causing issues.
                                            try:
                                                await member_mentions[0].remove_roles(role)
                                            except discord.errors.Forbidden:
                                                await message.channel.send(
                                                    "ERROR: Demote Error: Unable to remove the team owner role! Check permissions.")
                                                pass
                                            else:
                                                await message.channel.send(member_mentions[
                                                                               0].mention + " has been demoted from " + role.mention)

                                else:
                                    await message.channel.send(
                                        "Error: Demote Error: Only server staff and server owners can demote team owners!")

                            else:
                                await message.channel.send("Error: Demote Error: That user is not currently staff.")

                        else:
                            await message.channel.send("Error: Demote Error: That user is not on that team.")

            else:
                await message.channel.send("Error: Demote Error: You do not have permission to do that.")

        elif command == "servers":
            await message.channel.send("Currently connected to " + str(sum(1 for x in client.guilds)) + " servers.")

        elif command == "invite":
            await message.channel.send(
                "To invite this bot, please read the offical installation guide!\nhttps://docs.google.com/document/d/1fWUxzH0I0tPnonFlG6rDVMEq32ZTTbjsDXAhxHoEVqE/edit?usp=sharing\n\nThe development server can be found here:\n<https://discord.gg/ZVJasmz>")

        elif command == "help":
            pl = "`MagicLeague 2 Help Guide`\n" + \
                 "`getid <@member, @role, #channel>` Returns the ID of a mentioned role, member, or channel.\n" + \
                 "`sign <@member> <@team>/\"Name of Team\"` Sign a free agent to your team.\n" + \
                 "`release <@member> <@team>\"Name of Team\"` Releases a member from your team.\n" + \
                 "`promote <@member> <@team> <@team_staff_role>` Promotes a member of a team to the tagged team staff role.\n" + \
                 "`demote <@member> <@team>` Demotes a team staff member.\n" + \
                 "`servers` Returns the number of servers the bot is currently connected to.\n" + \
                 "`invite` Returns a link to the offical install guide.\n" + \
                 "`help` Shows this text.\n" + \
                 "`MagicLeague 2 version: " + __version__ + "`"
            await message.channel.send(pl)
        else:
            logger.info("Ignoring invalid command.")


# Run client.
client.run('')
