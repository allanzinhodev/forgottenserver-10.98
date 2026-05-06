dofile('data/npc/lib/npcsystem/npcsystem.lua')
local keywordHandler = KeywordHandler:new()
local npcHandler = NpcHandler:new(keywordHandler)
NpcSystem.parseParameters(npcHandler)

local TopicState = {}

-- OTServ event handling functions start
function onCreatureAppear(cid)              npcHandler:onCreatureAppear(cid) end
function onCreatureDisappear(cid)           npcHandler:onCreatureDisappear(cid) end
function onCreatureSay(cid, type, msg)      npcHandler:onCreatureSay(cid, type, msg) end
function onPlayerEndTrade(cid)              npcHandler:onPlayerEndTrade(cid) end
function onPlayerCloseChannel(cid)          npcHandler:onPlayerCloseChannel(cid) end
function onThink()                          npcHandler:onThink() end
-- OTServ event handling functions end



function creatureSayCallback(cid, type, msg)

	if (msgcontains(msg, "hello") or msgcontains(msg, "hi")) and (not npcHandler:isFocused(cid)) then
		npcHandler:say("Ol, como posso ajuda-lo?", cid)
		npcHandler:addFocus(cid)
		TopicState[cid] = 0

	elseif(not npcHandler:isFocused(cid)) then
		return false

	elseif msgcontains(msg, "bye") or msgcontains(msg, "farewell") then
		npcHandler:say("At mais, volte sempre que necessrio.", cid, TRUE)
		npcHandler:releaseFocus(cid)

	elseif msgcontains(msg, "team") and TopicState[cid] == 0 then
		npcHandler:say("Voc deseja virar sensei e ter seu proprio team?", cid)
		TopicState[cid] = 1

	elseif msgcontains(msg, "sim") or msgcontains(msg, "yes") and TopicState[cid] == 1 then
        gstat = getPlayerGuildRank(cid)
  		if gstat == "" then
            npcHandler:say("Ok, ento qual ser o nome do seu team?", cid)
	        TopicState[cid] = 2
  		elseif gstat == "Member" or gstat == "Vice" or gstat == "Leader" or gstat == "Sensei" then
  			npcHandler:say("Desculpa, mas voc j  membro de um team.", cid)
  		    npcHandler:releaseFocus(cid)
        end
	    
 	elseif TopicState[cid] == 2 then
 	    minLen = getConfigValue('guildNameMinLength')
        maxLen = getConfigValue('guildNameMaxLength')    
        if ((string.len(msg) >= minLen) and (string.len(msg) <= maxLen)) then
    		if (not(getGuildId(msg))) then
    		   doCreatureExecuteTalkAction(cid, "!createguild " .. msg, true)
    		   npcHandler:say("Pronto, para saber os comandos do seu Team diga {!commands} no chat do seu Team.", cid)
    		   npcHandler:releaseFocus(cid)
            else
               npcHandler:say("J existe um team com esse nome.", cid) 
            end
        else
               npcHandler:say("O nome do team deve ter entre "..minLen.." e "..maxLen.." caracteres.", cid)
        end
	end

	return true

end

npcHandler:setCallback(CALLBACK_MESSAGE_DEFAULT, creatureSayCallback)
npcHandler:setMessage(MESSAGE_WALKAWAY, "Sem educao!")
npcHandler:setMessage(MESSAGE_IDLETIMEOUT, "At mais ento.")