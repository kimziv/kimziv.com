---
layout: post
category : blog
tags : []
---
{% include JB/setup %}

####client下线 

    <presence type="unavailable">  
    <status>Logged out</status>  
    </presence>  

####client发起连接  
    <?xml version="1.0"?>  
    <stream:stream xmlns:stream="http://etherx.jabber.org/streams" version="1.0" xmlns="jabber:client" to="xumatomacbook-pro.local" xml:lang="en" xmlns:xml="http://www.w3.org/XML/1998/namespace">  

####server相应并回复验证的features  
    <?xml version='1.0'?><stream:stream xmlns='jabber:client' xmlns:stream='http://etherx.jabber.org/streams' from='xumatomacbook-pro.local' id='675c6847-c13d-4710-9844-d9339e4df087' version='1.0' xml:lang='en'>  
      
    <stream:features>  
    <ver xmlns="urn:xmpp:features:rosterver"/>  
    <starttls xmlns="urn:ietf:params:xml:ns:xmpp-tls"/>  
    <mechanisms xmlns="urn:ietf:params:xml:ns:xmpp-sasl">  
    <mechanism>PLAIN</mechanism>  
    <mechanism>ANONYMOUS</mechanism>  
    </mechanisms>  
    <register xmlns="http://jabber.org/features/iq-register"/>  
    <auth xmlns="http://jabber.org/features/iq-auth"/>  
    </stream:features>  

####client启动tls验证  
    <starttls xmlns="urn:ietf:params:xml:ns:xmpp-tls"/>  

####server表示支持，可以继续  
    <proceed xmlns="urn:ietf:params:xml:ns:xmpp-tls"/>  

####tls验证结束，重新开始  
    <?xml version="1.0"?>  
      
    <stream:stream xmlns:stream="http://etherx.jabber.org/streams" version="1.0" xmlns="jabber:client" to="xumatomacbook-pro.local" xml:lang="en" xmlns:xml="http://www.w3.org/XML/1998/namespace">  

####server响应，并返回下一步验证支持的features,sasl  
    <?xml version='1.0'?><stream:stream xmlns='jabber:client' xmlns:stream='http://etherx.jabber.org/streams' from='xumatomacbook-pro.local' id='675c6847-c13d-4710-9844-d9339e4df087' version='1.0' xml:lang='en'>  
      
      
    <stream:features>  
    <ver xmlns="urn:xmpp:features:rosterver"/>  
    <mechanisms xmlns="urn:ietf:params:xml:ns:xmpp-sasl">  
    <mechanism>PLAIN</mechanism>  
    <mechanism>ANONYMOUS</mechanism>  
    </mechanisms>  
    <register xmlns="http://jabber.org/features/iq-register"/>  
    <auth xmlns="http://jabber.org/features/iq-auth"/>  
    </stream:features>  

####client开始sasl验证  
    <auth xmlns="urn:ietf:params:xml:ns:xmpp-sasl" mechanism="PLAIN">AGd1YW5mZWkAZ3VhbmZlaQ==</auth>  

####server表示成功了  
    <success xmlns="urn:ietf:params:xml:ns:xmpp-sasl"/>  

####client重新开始  
    <?xml version="1.0"?>  
      
      
    <stream:stream xmlns:stream="http://etherx.jabber.org/streams" version="1.0" xmlns="jabber:client" to="xumatomacbook-pro.local" xml:lang="en" xmlns:xml="http://www.w3.org/XML/1998/namespace">  

####server响应并返回支持的features  
    <?xml version='1.0'?><stream:stream xmlns='jabber:client' xmlns:stream='http://etherx.jabber.org/streams' from='xumatomacbook-pro.local' id='675c6847-c13d-4710-9844-d9339e4df087' version='1.0' xml:lang='en'>  
      
      
    <stream:features>  
    <ver xmlns="urn:xmpp:features:rosterver"/>  
    <session xmlns="urn:ietf:params:xml:ns:xmpp-session"/>  
    <register xmlns="http://jabber.org/features/iq-register"/>  
    <bind xmlns="urn:ietf:params:xml:ns:xmpp-bind"/>  
    </stream:features>  

####client请求resource bind  
    <iq type="set" id="bind_1">  
    <bind xmlns="urn:ietf:params:xml:ns:xmpp-bind">  
    <resource>Psi+</resource>  
    </bind>  
    </iq>  

####server判断并返回结果  
    <iq xmlns="jabber:client" type="result" id="bind_1" to="guanfei@xumatomacbook-pro.local/Psi+">  
    <bind xmlns="urn:ietf:params:xml:ns:xmpp-bind">  
    <jid>guanfei@xumatomacbook-pro.local/Psi+</jid>  
    </bind>  
    </iq>  

####client发起session  
    <iq type="set" id="ab46a">  
    <session xmlns="urn:ietf:params:xml:ns:xmpp-session"/>  
    </iq>  

####server端响应  
    <iq type="result" id="ab46a" to="guanfei@xumatomacbook-pro.local/Psi+"/>  

    ####client端请求roster列表  
    <iq type="get" id="ab47a">  
    <query xmlns="jabber:iq:roster"/>  
    </iq>  

####server端返回  
    <iq type="result" id="ab47a" to="guanfei@xumatomacbook-pro.local/Psi+">  
    <query xmlns="jabber:iq:roster">  
    <item subscription="both" name="ohno" jid="guanfei1@xumatomacbook-pro.local"/>  
    </query>  
    </iq>  

####client广播自己的出席信息  
    <presence>  
    <priority>50</priority>  
    <c xmlns="http://jabber.org/protocol/caps" node="http://psi-dev.googlecode.com/caps" ver="0.16" ext="ca cs e-time ep-notify-2 html last-act mr sxe whiteboard"/>  
    </presence>  

####client请求自己的个人信息  
    <iq type="get" id="ab49a">  
    <query xmlns="jabber:iq:privacy"/>  
    </iq>  

####client请求bookmark  
    <iq type="get" id="ab4aa">  
    <query xmlns="jabber:iq:private">  
    <storage xmlns="storage:bookmarks"/>  
    </query>  
    </iq>  

####client请求个人vcard  
    <iq type="get" to="guanfei@xumatomacbook-pro.local" id="ab4ba">  
    <vCard xmlns="vcard-temp"/>  
    </iq>  

####client请求disco列表  
    <iq type="get" to="xumatomacbook-pro.local" id="ab4ca">  
    <query xmlns="http://jabber.org/protocol/disco#info"/>  
    </iq>  

####server广播出席信息  
    <presence from="guanfei@xumatomacbook-pro.local/Psi+" to="guanfei@xumatomacbook-pro.local">  
    <priority>50</priority>  
    <c xmlns="http://jabber.org/protocol/caps" node="http://psi-dev.googlecode.com/caps" ver="0.16" ext="ca cs e-time ep-notify-2 html last-act mr sxe whiteboard"/>  
    </presence>  

####server返回个人信息项列表  
    <iq type="result" id="ab49a" to="guanfei@xumatomacbook-pro.local/Psi+">  
    <query xmlns="jabber:iq:privacy">  
    <list name="blocked"/>  
    <default name="blocked"/>  
    <active name="blocked"/>  
    </query>  
    </iq>  

####client请求block项内容  
    <iq type="get" id="ab4da">  
    <query xmlns="jabber:iq:privacy">  
    <list name="blocked"/>  
    </query>  
    </iq>  

####server返回bookmark信息  
    <iq type="result" id="ab4aa" to="guanfei@xumatomacbook-pro.local/Psi+">  
    <query xmlns="jabber:iq:private">  
    <storage xmlns="storage:bookmarks"/>  
    </query>  
    </iq>  

####server返回vcard信息  
    <iq from="guanfei@xumatomacbook-pro.local" type="result" to="guanfei@xumatomacbook-pro.local/Psi+" id="ab4ba">  
    <vCard xmlns="vcard-temp">  
    <FN>guanfei</FN>  
    <NICKNAME>guanfei</NICKNAME>  
    </vCard>  
    </iq>  

####server返回disco列表  
    <iq from="xumatomacbook-pro.local" type="result" to="guanfei@xumatomacbook-pro.local/Psi+" id="ab4ca">  
    <query xmlns="http://jabber.org/protocol/disco#info">  
    <identity category="server" type="im" name="Tigase ver. 0.0.0-0"/>  
    <feature var="http://jabber.org/protocol/disco#info"/>  
    <feature var="http://jabber.org/protocol/disco#items"/>  
    <feature var="msgoffline"/>  
    <feature var="http://jabber.org/protocol/stats"/>  
    <feature var="http://jabber.org/protocol/commands"/>  
    <feature var="jabber:iq:version"/>  
    <feature var="jabber:iq:roster"/>  
    <feature var="jabber:iq:roster-dynamic"/>  
    <feature var="vcard-temp"/>  
    <feature var="urn:ietf:params:xml:ns:xmpp-sasl"/>  
    <feature var="urn:xmpp:ping"/>  
    <feature var="http://jabber.org/protocol/pubsub"/>  
    <feature var="http://jabber.org/protocol/pubsub#owner"/>  
    <feature var="http://jabber.org/protocol/pubsub#publish"/>  
    <identity category="pubsub" type="pep"/>  
    <feature var="urn:ietf:params:xml:ns:xmpp-session"/>  
    <feature var="http://jabber.org/protocol/amp"/>  
    <feature var="msgoffline"/>  
    <feature var="http://jabber.org/protocol/disco#info"/>  
    <feature var="http://jabber.org/protocol/disco#items"/>  
    <feature var="jabber:iq:privacy"/>  
    <feature var="urn:ietf:params:xml:ns:xmpp-bind"/>  
    <feature var="jabber:iq:private"/>  
    <feature var="jabber:iq:auth"/>  
    </query>  
    </iq>  
#### 

    <presence from="guanfei1@xumatomacbook-pro.local/Psi+" to="guanfei@xumatomacbook-pro.local">  
    <priority>50</priority>  
    <c xmlns="http://jabber.org/protocol/caps" node="http://psi-dev.googlecode.com/caps" ver="0.16" ext="ca cs e-time ep-notify-2 html last-act mr sxe whiteboard"/>  
    </presence>  
    
#### 

    <iq type="result" id="ab4da" to="guanfei@xumatomacbook-pro.local/Psi+">  
    <query xmlns="jabber:iq:privacy">  
    <list name="blocked">  
    <item action="allow" order="100"/>  
    </list>  
    </query>  
    </iq>  