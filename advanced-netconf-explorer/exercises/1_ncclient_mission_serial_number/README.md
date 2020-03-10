## Objectives
* Open a NETCONF session using `ncclient`,
* Get the running-configuration (XML) from the device

## Files that need to be edited

* `run.py`
    * Getting the device information from the devices.yaml file
        * Store this information in a variable (e.g : xe_sandbox)
    * Using ncclient to get the running-config of the device, as xml
        * Replace the EXERCISE by the correct value of the xe_sandbox dictionnary.

## Available methods of ncclient manager

Operations are defined [here](https://github.com/ncclient/ncclient/tree/master/ncclient/operations).

```
OPERATIONS = {
    "get": operations.Get,
    "get_config": operations.GetConfig,
    "get_schema": operations.GetSchema,
    "dispatch": operations.Dispatch,
    "edit_config": operations.EditConfig,
    "copy_config": operations.CopyConfig,
    "validate": operations.Validate,
    "commit": operations.Commit,
    "discard_changes": operations.DiscardChanges,
    "cancel_commit": operations.CancelCommit,
    "delete_config": operations.DeleteConfig,
    "lock": operations.Lock,
    "unlock": operations.Unlock,
    "create_subscription": operations.CreateSubscription,
    "close_session": operations.CloseSession,
    "kill_session": operations.KillSession,
    "poweroff_machine": operations.PoweroffMachine,
    "reboot_machine": operations.RebootMachine,
}
```
        
## Example of expected outputs

```xml
Configuration =
<?xml version="1.0" ?>
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<version>16.11</version>
		<boot-start-marker/>
		<boot-end-marker/>
		<banner>
			<motd>
				<banner>^C</banner>
			</motd>
		</banner>
		<memory>
			<free>
				<low-watermark>
					<processor>80557</processor>
				</low-watermark>
			</free>
		</memory>
		<call-home>
			<contact-email-addr xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-call-home">sch-smart-licensing@cisco.com</contact-email-addr>
			<profile xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-call-home">
				<profile-name>CiscoTAC-1</profile-name>
				<active>true</active>
			</profile>
		</call-home>
		<service>
			<timestamps>
				<debug>
					<datetime>
						<msec/>
					</datetime>
				</debug>
				<log>
					<datetime>
						<msec/>
					</datetime>
				</log>
			</timestamps>
			<call-home/>
		</service>
		<platform>
			<console xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
				<output>virtual</output>
			</console>
		</platform>
		<hostname>csr1000v-1</hostname>
		<enable>
			<secret>
				<type>9</type>
				<secret>$9$PvdeTeuxxh0ygk$PSg0GTG2I7bluI51e.IvfEu2uxy56e/9/PgqzFUklso</secret>
			</secret>
		</enable>
		<username>
			<name>cisco</name>
			<privilege>15</privilege>
			<secret>
				<encryption>9</encryption>
				<secret>$9$COf3Q4xfzT.JxE$L3hvSkDv874Qrh8Hzdv/rPQjLNOjreYG2ocffHG7rls</secret>
			</secret>
		</username>
		<username>
			<name>developer</name>
			<privilege>15</privilege>
			<secret>
				<encryption>9</encryption>
				<secret>$9$fhUXi6Xg438iAE$..VhXRCHiDQy3K2zmZUl9iZLbQJ9wpUtQZwQxSRESc2</secret>
			</secret>
		</username>
		<username>
			<name>root</name>
			<privilege>15</privilege>
			<secret>
				<encryption>9</encryption>
				<secret>$9$FfUDIPBFcs03AE$MyLIWEuiRle8p3yGflAGTcrJA6BUUh/oWtyyfoMQXSI</secret>
			</secret>
		</username>
		<username>
			<name>teset_md5</name>
			<secret>
				<encryption>5</encryption>
				<secret>$1$pdQG$blOvq4Ey0SJCv3n001vnj.</secret>
			</secret>
		</username>
		<username>
			<name>teset_type8</name>
			<secret>
				<encryption>8</encryption>
				<secret>$8$FiJQlYEnyjCvkk$GkMYqqmLNP2YNoAFBcod4Tg7/Sy6e58Q3a8umokmlJI</secret>
			</secret>
		</username>
		<username>
			<name>teset_type9</name>
			<secret>
				<encryption>9</encryption>
				<secret>$9$8OnHa3BCA8nvl.$guLZp0qgTdyTma10Tk.O7iUO5NufJhOnDoUcvy1R79I</secret>
			</secret>
		</username>
		<ip>
			<domain>
				<name>abc.inc</name>
			</domain>
			<forward-protocol>
				<protocol>nd</protocol>
			</forward-protocol>
			<route>
				<ip-route-interface-forwarding-list>
					<prefix>0.0.0.0</prefix>
					<mask>0.0.0.0</mask>
					<fwd-list>
						<fwd>GigabitEthernet1</fwd>
						<interface-next-hop>
							<ip-address>10.10.20.254</ip-address>
						</interface-next-hop>
					</fwd-list>
				</ip-route-interface-forwarding-list>
			</route>
			<scp>
				<server>
					<enable/>
				</server>
			</scp>
			<ssh>
				<rsa>
					<keypair-name>ssh-key</keypair-name>
				</rsa>
				<version>2</version>
			</ssh>
			<access-list>
				<extended xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
					<name>meraki-fqdn-dns</name>
				</extended>
				<extended xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
					<name>197</name>
					<access-list-seq-rule>
						<sequence>10</sequence>
						<ace-rule>
							<action>permit</action>
							<protocol>tcp</protocol>
							<any/>
							<dst-any/>
							<dst-eq>1494</dst-eq>
						</ace-rule>
					</access-list-seq-rule>
					<access-list-seq-rule>
						<sequence>20</sequence>
						<ace-rule>
							<action>permit</action>
							<protocol>tcp</protocol>
							<any/>
							<dst-any/>
							<dst-eq>1604</dst-eq>
						</ace-rule>
					</access-list-seq-rule>
					<access-list-seq-rule>
						<sequence>30</sequence>
						<ace-rule>
							<action>permit</action>
							<protocol>udp</protocol>
							<any/>
							<dst-any/>
							<dst-eq>1494</dst-eq>
						</ace-rule>
					</access-list-seq-rule>
					<access-list-seq-rule>
						<sequence>40</sequence>
						<ace-rule>
							<action>permit</action>
							<protocol>udp</protocol>
							<any/>
							<dst-any/>
							<dst-eq>1604</dst-eq>
						</ace-rule>
					</access-list-seq-rule>
					<access-list-seq-rule>
						<sequence>50</sequence>
						<ace-rule>
							<action>permit</action>
							<protocol>tcp</protocol>
							<any/>
							<dst-any/>
							<dst-eq>3389</dst-eq>
						</ace-rule>
					</access-list-seq-rule>
				</extended>
			</access-list>
			<http xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-http">
				<authentication>
					<local/>
				</authentication>
				<server>true</server>
				<secure-server>true</secure-server>
			</http>
		</ip>
		<interface>
			<GigabitEthernet>
				<name>1</name>
				<description>MANAGEMENT INTERFACE - DON'T TOUCH ME</description>
				<ip>
					<address>
						<primary>
							<address>10.10.20.48</address>
							<mask>255.255.255.0</mask>
						</primary>
					</address>
				</ip>
				<mop>
					<enabled>false</enabled>
					<sysid>false</sysid>
				</mop>
				<negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
					<auto>true</auto>
				</negotiation>
			</GigabitEthernet>
			<GigabitEthernet>
				<name>2</name>
				<description>Network Interface</description>
				<shutdown/>
				<mop>
					<enabled>false</enabled>
					<sysid>false</sysid>
				</mop>
				<negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
					<auto>true</auto>
				</negotiation>
			</GigabitEthernet>
			<GigabitEthernet>
				<name>3</name>
				<description>Network Interface</description>
				<shutdown/>
				<mop>
					<enabled>false</enabled>
					<sysid>false</sysid>
				</mop>
				<negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
					<auto>true</auto>
				</negotiation>
			</GigabitEthernet>
			<Loopback>
				<name>0</name>
				<description>[VOIP BINDING INTERFACE]</description>
				<ip>
					<address>
						<primary>
							<address>1.1.1.1</address>
							<mask>255.255.255.255</mask>
						</primary>
					</address>
					<proxy-arp>false</proxy-arp>
					<redirects>false</redirects>
				</ip>
			</Loopback>
			<Loopback>
				<name>98</name>
				<shutdown/>
			</Loopback>
			<Loopback>
				<name>99</name>
				<shutdown/>
			</Loopback>
			<Loopback>
				<name>666</name>
			</Loopback>
			<Loopback>
				<name>667</name>
			</Loopback>
		</interface>
		<control-plane/>
		<login>
			<on-success>
				<log/>
			</on-success>
		</login>
		<multilink>
			<bundle-name xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ppp">authenticated</bundle-name>
		</multilink>
		<redundancy/>
		<spanning-tree>
			<extend xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-spanning-tree">
				<system-id/>
			</extend>
		</spanning-tree>
		<subscriber>
			<templating/>
		</subscriber>
		<crypto>
			<pki xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-crypto">
				<certificate>
					<chain>
						<name>SLA-TrustPoint</name>
						<certificate>
							<serial>01</serial>
							<certtype>ca</certtype>
						</certificate>
					</chain>
					<chain>
						<name>TP-self-signed-1059130051</name>
						<certificate>
							<serial>01</serial>
							<certtype>self-signed</certtype>
						</certificate>
					</chain>
				</certificate>
				<trustpoint>
					<id>SLA-TrustPoint</id>
					<enrollment>
						<pkcs12/>
					</enrollment>
					<revocation-check>crl</revocation-check>
				</trustpoint>
				<trustpoint>
					<id>TP-self-signed-1059130051</id>
					<enrollment>
						<selfsigned/>
					</enrollment>
					<revocation-check>none</revocation-check>
					<subject-name>cn=IOS-Self-Signed-Certificate-1059130051</subject-name>
				</trustpoint>
			</pki>
		</crypto>
		<license>
			<udi>
				<pid>CSR1000V</pid>
				<sn>9SDBK8AK3H9</sn>
			</udi>
			<boot>
				<level>
					<ax/>
				</level>
			</boot>
		</license>
		<line>
			<console>
				<first>0</first>
				<exec-timeout>
					<minutes>0</minutes>
					<seconds>0</seconds>
				</exec-timeout>
				<stopbits>1</stopbits>
			</console>
			<vty>
				<first>0</first>
				<last>4</last>
				<login>
					<local/>
				</login>
				<transport>
					<input>
						<input>ssh</input>
					</input>
				</transport>
			</vty>
		</line>
		<ntp>
			<server xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ntp">
				<server-list>
					<ip-address>10.0.0.1</ip-address>
				</server-list>
				<server-list>
					<ip-address>10.0.0.2</ip-address>
				</server-list>
				<server-list>
					<ip-address>10.0.0.3</ip-address>
				</server-list>
				<server-list>
					<ip-address>10.0.0.4</ip-address>
				</server-list>
			</server>
		</ntp>
		<diagnostic xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-diagnostics">
			<bootup>
				<level>minimal</level>
			</bootup>
		</diagnostic>
		<et-analytics xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-eta"/>
	</native>
	<licensing xmlns="http://cisco.com/ns/yang/cisco-smart-license">
		<config>
			<enable>false</enable>
			<privacy>
				<hostname>false</hostname>
				<version>false</version>
			</privacy>
			<utility>
				<utility-enable>false</utility-enable>
			</utility>
		</config>
	</licensing>
	<acl xmlns="http://openconfig.net/yang/acl">
		<acl-sets>
			<acl-set>
				<name>meraki-fqdn-dns</name>
				<type>ACL_IPV4</type>
				<config>
					<name>meraki-fqdn-dns</name>
					<type>ACL_IPV4</type>
				</config>
			</acl-set>
			<acl-set>
				<name>197</name>
				<type>ACL_IPV4</type>
				<config>
					<name>197</name>
					<type>ACL_IPV4</type>
				</config>
				<acl-entries>
					<acl-entry>
						<sequence-id>10</sequence-id>
						<config>
							<sequence-id>10</sequence-id>
						</config>
						<ipv4>
							<config>
								<protocol xmlns:oc-pkt-match-types="http://openconfig.net/yang/packet-match-types">oc-pkt-match-types:IP_TCP</protocol>
							</config>
						</ipv4>
						<transport>
							<config>
								<source-port>ANY</source-port>
								<destination-port>1494</destination-port>
							</config>
						</transport>
						<actions>
							<config>
								<forwarding-action>ACCEPT</forwarding-action>
								<log-action>LOG_NONE</log-action>
							</config>
						</actions>
					</acl-entry>
					<acl-entry>
						<sequence-id>20</sequence-id>
						<config>
							<sequence-id>20</sequence-id>
						</config>
						<ipv4>
							<config>
								<protocol xmlns:oc-pkt-match-types="http://openconfig.net/yang/packet-match-types">oc-pkt-match-types:IP_TCP</protocol>
							</config>
						</ipv4>
						<transport>
							<config>
								<source-port>ANY</source-port>
								<destination-port>1604</destination-port>
							</config>
						</transport>
						<actions>
							<config>
								<forwarding-action>ACCEPT</forwarding-action>
								<log-action>LOG_NONE</log-action>
							</config>
						</actions>
					</acl-entry>
					<acl-entry>
						<sequence-id>30</sequence-id>
						<config>
							<sequence-id>30</sequence-id>
						</config>
						<ipv4>
							<config>
								<protocol xmlns:oc-pkt-match-types="http://openconfig.net/yang/packet-match-types">oc-pkt-match-types:IP_UDP</protocol>
							</config>
						</ipv4>
						<transport>
							<config>
								<source-port>ANY</source-port>
								<destination-port>1494</destination-port>
							</config>
						</transport>
						<actions>
							<config>
								<forwarding-action>ACCEPT</forwarding-action>
								<log-action>LOG_NONE</log-action>
							</config>
						</actions>
					</acl-entry>
					<acl-entry>
						<sequence-id>40</sequence-id>
						<config>
							<sequence-id>40</sequence-id>
						</config>
						<ipv4>
							<config>
								<protocol xmlns:oc-pkt-match-types="http://openconfig.net/yang/packet-match-types">oc-pkt-match-types:IP_UDP</protocol>
							</config>
						</ipv4>
						<transport>
							<config>
								<source-port>ANY</source-port>
								<destination-port>1604</destination-port>
							</config>
						</transport>
						<actions>
							<config>
								<forwarding-action>ACCEPT</forwarding-action>
								<log-action>LOG_NONE</log-action>
							</config>
						</actions>
					</acl-entry>
					<acl-entry>
						<sequence-id>50</sequence-id>
						<config>
							<sequence-id>50</sequence-id>
						</config>
						<ipv4>
							<config>
								<protocol xmlns:oc-pkt-match-types="http://openconfig.net/yang/packet-match-types">oc-pkt-match-types:IP_TCP</protocol>
							</config>
						</ipv4>
						<transport>
							<config>
								<source-port>ANY</source-port>
								<destination-port>3389</destination-port>
							</config>
						</transport>
						<actions>
							<config>
								<forwarding-action>ACCEPT</forwarding-action>
								<log-action>LOG_NONE</log-action>
							</config>
						</actions>
					</acl-entry>
				</acl-entries>
			</acl-set>
		</acl-sets>
	</acl>
	<interfaces xmlns="http://openconfig.net/yang/interfaces">
		<interface>
			<name>GigabitEthernet1</name>
			<config>
				<name>GigabitEthernet1</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
				<description>MANAGEMENT INTERFACE - DON'T TOUCH ME</description>
				<enabled>true</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<description>MANAGEMENT INTERFACE - DON'T TOUCH ME</description>
						<enabled>true</enabled>
					</config>
					<ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
						<addresses>
							<address>
								<ip>10.10.20.48</ip>
								<config>
									<ip>10.10.20.48</ip>
									<prefix-length>24</prefix-length>
								</config>
							</address>
						</addresses>
					</ipv4>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
			<ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
				<config>
					<mac-address>00:50:56:bb:e9:9c</mac-address>
					<auto-negotiate>true</auto-negotiate>
				</config>
			</ethernet>
		</interface>
		<interface>
			<name>GigabitEthernet2</name>
			<config>
				<name>GigabitEthernet2</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
				<description>Network Interface</description>
				<enabled>false</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<description>Network Interface</description>
						<enabled>false</enabled>
					</config>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
			<ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
				<config>
					<mac-address>00:50:56:bb:77:1a</mac-address>
					<auto-negotiate>true</auto-negotiate>
				</config>
			</ethernet>
		</interface>
		<interface>
			<name>GigabitEthernet3</name>
			<config>
				<name>GigabitEthernet3</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
				<description>Network Interface</description>
				<enabled>false</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<description>Network Interface</description>
						<enabled>false</enabled>
					</config>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
			<ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
				<config>
					<mac-address>00:50:56:bb:eb:1e</mac-address>
					<auto-negotiate>true</auto-negotiate>
				</config>
			</ethernet>
		</interface>
		<interface>
			<name>Loopback0</name>
			<config>
				<name>Loopback0</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
				<description>[VOIP BINDING INTERFACE]</description>
				<enabled>true</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<description>[VOIP BINDING INTERFACE]</description>
						<enabled>true</enabled>
					</config>
					<ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
						<addresses>
							<address>
								<ip>1.1.1.1</ip>
								<config>
									<ip>1.1.1.1</ip>
									<prefix-length>32</prefix-length>
								</config>
							</address>
						</addresses>
						<proxy-arp>
							<config>
								<mode>DISABLE</mode>
							</config>
						</proxy-arp>
					</ipv4>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
		</interface>
		<interface>
			<name>Loopback98</name>
			<config>
				<name>Loopback98</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
				<enabled>false</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<enabled>false</enabled>
					</config>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
		</interface>
		<interface>
			<name>Loopback99</name>
			<config>
				<name>Loopback99</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
				<enabled>false</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<enabled>false</enabled>
					</config>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
		</interface>
		<interface>
			<name>Loopback666</name>
			<config>
				<name>Loopback666</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
				<enabled>true</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<enabled>true</enabled>
					</config>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
		</interface>
		<interface>
			<name>Loopback667</name>
			<config>
				<name>Loopback667</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
				<enabled>true</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<enabled>true</enabled>
					</config>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
		</interface>
	</interfaces>
	<lldp xmlns="http://openconfig.net/yang/lldp">
		<config>
			<enabled>false</enabled>
		</config>
		<interfaces>
			<interface>
				<name>GigabitEthernet1</name>
				<config>
					<name>GigabitEthernet1</name>
					<enabled>true</enabled>
				</config>
			</interface>
			<interface>
				<name>GigabitEthernet2</name>
				<config>
					<name>GigabitEthernet2</name>
					<enabled>true</enabled>
				</config>
			</interface>
			<interface>
				<name>GigabitEthernet3</name>
				<config>
					<name>GigabitEthernet3</name>
					<enabled>true</enabled>
				</config>
			</interface>
		</interfaces>
	</lldp>
	<network-instances xmlns="http://openconfig.net/yang/network-instance">
		<network-instance>
			<name>default</name>
			<config>
				<name>default</name>
				<type xmlns:oc-ni-types="http://openconfig.net/yang/network-instance-types">oc-ni-types:DEFAULT_INSTANCE</type>
				<description>default-vrf [read-only]</description>
			</config>
			<tables>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					</config>
				</table>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					</config>
				</table>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					</config>
				</table>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					</config>
				</table>
			</tables>
			<protocols>
				<protocol>
					<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</identifier>
					<name>DEFAULT</name>
					<config>
						<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</identifier>
						<name>DEFAULT</name>
					</config>
					<static-routes>
						<static>
							<prefix>0.0.0.0/0</prefix>
							<config>
								<prefix>0.0.0.0/0</prefix>
							</config>
							<next-hops>
								<next-hop>
									<index>GigabitEthernet1_10.10.20.254</index>
									<config>
										<index>GigabitEthernet1_10.10.20.254</index>
										<next-hop>10.10.20.254</next-hop>
									</config>
									<interface-ref>
										<config>
											<interface>GigabitEthernet1</interface>
										</config>
									</interface-ref>
								</next-hop>
							</next-hops>
						</static>
					</static-routes>
				</protocol>
				<protocol>
					<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</identifier>
					<name>DEFAULT</name>
					<config>
						<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</identifier>
						<name>DEFAULT</name>
					</config>
				</protocol>
			</protocols>
		</network-instance>
	</network-instances>
	<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>GigabitEthernet1</name>
			<description>MANAGEMENT INTERFACE - DON'T TOUCH ME</description>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>10.10.20.48</ip>
					<netmask>255.255.255.0</netmask>
				</address>
			</ipv4>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
		<interface>
			<name>GigabitEthernet2</name>
			<description>Network Interface</description>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
			<enabled>false</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
		<interface>
			<name>GigabitEthernet3</name>
			<description>Network Interface</description>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
			<enabled>false</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
		<interface>
			<name>Loopback0</name>
			<description>[VOIP BINDING INTERFACE]</description>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>1.1.1.1</ip>
					<netmask>255.255.255.255</netmask>
				</address>
			</ipv4>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
		<interface>
			<name>Loopback98</name>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>false</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
		<interface>
			<name>Loopback99</name>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>false</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
		<interface>
			<name>Loopback666</name>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
		<interface>
			<name>Loopback667</name>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
	</interfaces>
	<nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
		<enable-nacm>true</enable-nacm>
		<read-default>deny</read-default>
		<write-default>deny</write-default>
		<exec-default>deny</exec-default>
		<enable-external-groups>true</enable-external-groups>
		<rule-list>
			<name>admin</name>
			<group>PRIV15</group>
			<rule>
				<name>permit-all</name>
				<module-name>*</module-name>
				<access-operations>*</access-operations>
				<action>permit</action>
			</rule>
		</rule-list>
	</nacm>
	<routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
		<routing-instance>
			<name>default</name>
			<description>default-vrf [read-only]</description>
			<routing-protocols>
				<routing-protocol>
					<type>static</type>
					<name>1</name>
					<static-routes>
						<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ipv4-unicast-routing">
							<route>
								<destination-prefix>0.0.0.0/0</destination-prefix>
								<next-hop>
									<outgoing-interface>GigabitEthernet1</outgoing-interface>
								</next-hop>
							</route>
						</ipv4>
					</static-routes>
				</routing-protocol>
			</routing-protocols>
		</routing-instance>
	</routing>
</data>
```


