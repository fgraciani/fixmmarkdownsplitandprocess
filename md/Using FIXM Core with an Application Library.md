## Using FIXM Core with an Application Library

### Basic Message Application Library

The Basic Message Application Library is intended to enhance FIXM Core
by providing basic messaging support for users, including message types
and timestamps, as well as the ability to batch multiple flight messages
together into a single aggregate message. It also provides extension
hooks for users who wish to add their own custom messaging fields. Users
who only require this basic level of message support are encouraged to
use the Basic Message Application Library.

This application library contains two root fields that can be used as an
entry point: Message and MessageCollection.

<img src=".//media/image51.emf" style="width:5.99514in;height:3.93264in" />

When using Basic Message for data representation, all XML documents must
begin with one of these two elements. Similarly, like Fixm.xsd for Core,
the BasicMessage.xsd schema file is the root schema of the Basic Message
Application Library and is the file that should be referenced for
validation or use with any XML utilities.

Unlike FF-ICE Message, the Basic Message Application Library focuses
only on providing users with generic and reusable message data
structures. It does not provide any message template since it is not
linked to any particular operational use of FIXM.

Users who wish to include additional message data structures beyond what
is provided in Basic Message (but who do not wish to create templates
for a pre-defined set of messages) are encouraged to do so via creating
an Extension to Basic Message (see Section 4.3.1 and Section 4.3.3 below
for more on this). Users who wish to create message templates for their
systems are encouraged to do so via creating their own Application
Library (see Section 4.2.2 for details).

*Example: Batch Updates*

Returning to our fictitious user, XAS has launched a successful
departure and arrival alert service using FIXM Core alone but is now
interested in expanding their capabilities. Some of XAS’s consumers
suffer from network outages and have requested an additional service
which they could use to invoke a bulk update containing all the alerts
they might have missed during such an outage.

XAS determines that Basic Message should be sufficient to meet the needs
of this new service. The MessageCollection element allows XAS to batch
together as many alerts as needed for the update, and the timestamp
associated with each message provides the additional benefit of letting
the consumer know exactly when the alert had originally been sent. XAS
decides to construct all updates using MessageCollection as the root
element to make parsing the updates more consistent and instructs
recipients of these updates to validate the XML against
BasicMessage.xsd. Below is a snippet of what the XML payload of such an
update may look like.

&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;msg:MessageCollection xmlns:msg="http://www.fixm.aero/app/msg/1.0"
xmlns:fx="http://www.fixm.aero/flight/4.2"
xmlns:fb="http://www.fixm.aero/base/4.2"&gt;

&lt;msg:message&gt;

&lt;msg:flight&gt;

&lt;fx:departure&gt;

&lt;fx:actualTimeOfDeparture&gt;2020-01-01T00:03:00Z&lt;/fx:actualTimeOfDeparture&gt;

&lt;fx:aerodrome&gt;

&lt;fb:locationIndicator&gt;KBOS&lt;/fb:locationIndicator&gt;

&lt;/fx:aerodrome&gt;

&lt;/fx:departure&gt;

&lt;fx:flightIdentification&gt;

&lt;fx:aircraftIdentification&gt;ABC1234&lt;/fx:aircraftIdentification&gt;

&lt;/fx:flightIdentification&gt;

&lt;fx:gufi
codeSpace="urn:uuid"&gt;3e7f6a63-6c3b-4f0f-844b-4b84338ed103&lt;/fx:gufi&gt;

&lt;/msg:flight&gt;

&lt;msg:timestamp&gt;2020-01-01T00:03:01Z&lt;/msg:timestamp&gt;

&lt;msg:type&gt;DEPARTURE&lt;/msg:type&gt;

&lt;/msg:message&gt;

.

.

.

&lt;msg:message&gt;

&lt;msg:flight&gt;

&lt;fx:arrival&gt;

&lt;fx:actualTimeOfArrival&gt;2020-01-01T23:58:00Z&lt;/fx:actualTimeOfArrival&gt;

&lt;fx:arrivalAerodrome&gt;

&lt;fb:locationIndicator&gt;KLAX&lt;/fb:locationIndicator&gt;

&lt;/fx:arrivalAerodrome&gt;

&lt;/fx:arrival&gt;

&lt;fx:flightIdentification&gt;

&lt;fx:aircraftIdentification&gt;XYZ1234&lt;/fx:aircraftIdentification&gt;

&lt;/fx:flightIdentification&gt;

&lt;fx:gufi
codeSpace="urn:uuid"&gt;3808e010-3c24-4a04-afd2-f62ba9ec43f6&lt;/fx:gufi&gt;

&lt;/msg:flight&gt;

&lt;msg:timestamp&gt;2020-01-01T23:58:01Z&lt;/msg:timestamp&gt;

&lt;msg:type&gt;ARRIVAL&lt;/msg:type&gt;

&lt;/msg:message&gt;

&lt;msg:timestamp&gt;2020-01-02T00:05:00Z&lt;/msg:timestamp&gt;

&lt;msg:type&gt;BULK\_UPDATE&lt;/msg:type&gt;

&lt;/msg:MessageCollection&gt;

### Creating an Application Library

If the organization of Basic Message does not suit the user’s data
exchange or if the user wants to create message templates to more fully
lock down and describe their message structures and content, they should
consider creating their own custom Application Library.

As described in Section 2.2.2 above, Application Libraries enhance FIXM
Core by adding context specific message data structures and as well as
stricter validation rules via message templates. An Application should
define its own namespace to distinguish it from FIXM Core as well as
creating one or more root elements to be used as an entry point into the
Library. If the Application includes message templates, it may have more
than one root schema: one for using the Application Library alone with
no further restrictions and one (or more) for use with the templates.
The FF-ICE Message Application Library is a good example of this, with
users referencing FficeMessage.xsd for unrestricted use of the Library,
FficeTemplates.xsd for making use of all thirteen templates used to
represent the FF-ICE messages, or one of the thirteen template-specific
schemas files corresponding to each FF-ICE message.

While the content and organization of an Application Library depends
entirely on the needs of the data exchange it is intended to support,
the FF-ICE Message Application and Basic Message Libraries should
provide a useful set of examples for how to build a Library with and
without associated templates. To supplement this, Appendix A below
provides step-by-step instructions on how to create a simple
Application.

*Example: Upgraded Alerts*

At this point, our fictitious user XAS has decided to upgrade their
original alert service to be able to send departure and arrival messages
to specific recipients (rather than maintaining a single, common
endpoint for all consumers) as well as making use of templates to
clearly lockdown the expected format of the alert messages. To
accomplish this, XAS decides to create their own Application Library.

This custom Application Library defines its own namespace
(“http://www.fixm.aero/app/example/1.0”) and root
element(“ExampleMessage”) as well as a number of header fields needed to
represent data XAS wants to exchange with each alert (“sender”,
“recipient”, “timestamp”, and “type”). XAS then goes on to create two
templates: one that locks down the content of a departure alert and
another for the arrival alert. Details on how to build this Application
Library along with more specifics as to its content are supplied below
in Appendix A.

With the Application Library built, XAS instructs consumers to make use
of the ExampleTemplates.xsd file described in Appendix A when validating
the new alert messages. Below is an example of how the XML payload of
one of the new arrival alert messages coming from this service may
appear.

&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;xmg:ExampleMessage xsi:type="xmg:ExampleDA\_ExampleMessageType"
xmlns:xmg="http://www.fixm.aero/app/example/1.0"
xmlns:fb="http://www.fixm.aero/base/4.2"
xmlns:fx="http://www.fixm.aero/flight/4.2"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;

&lt;xmg:flight&gt;

&lt;fx:departure&gt;

&lt;fx:actualTimeOfDeparture&gt;1903-12-17T03:35:00Z&lt;/fx:actualTimeOfDeparture&gt;

&lt;fx:aerodrome&gt;

&lt;fb:name&gt;KILL DEVIL HILL&lt;/fb:name&gt;

&lt;fb:referencePoint srsName="urn:ogc:def:crs:EPSG::4326"&gt;

&lt;fb:pos&gt;36.019970 -75.668760&lt;/fb:pos&gt;

&lt;/fb:referencePoint&gt;

&lt;/fx:aerodrome&gt;

&lt;/fx:departure&gt;

&lt;fx:flightIdentification&gt;

&lt;fx:aircraftIdentification&gt;WRF01&lt;/fx:aircraftIdentification&gt;

&lt;/fx:flightIdentification&gt;

&lt;fx:gufi
codeSpace="urn:uuid"&gt;18611e54-52b8-4fb5-a2fa-12173b1d39db&lt;/fx:gufi&gt;

&lt;/xmg:flight&gt;

&lt;xmg:recipient&gt;

&lt;fb:name&gt;HISTORY&lt;/fb:name&gt;

&lt;/xmg:recipient&gt;

&lt;xmg:sender&gt;

&lt;fb:name&gt;ORVILLE WRIGHT&lt;/fb:name&gt;

&lt;/xmg:sender&gt;

&lt;xmg:timestamp&gt;2020-01-15T17:20:33Z&lt;/xmg:timestamp&gt;

&lt;xmg:type&gt;DEPARTURE&lt;/xmg:type&gt;

&lt;/xmg:ExampleMessage&gt;

