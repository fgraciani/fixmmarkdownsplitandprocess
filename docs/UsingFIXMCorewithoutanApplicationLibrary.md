## Using FIXM Core without an Application Library

In some cases, the nature of the messaging infrastructure employed for a
particular data exchange makes the use of Application Libraries
unnecessary or irrelevant (perhaps due to the infrastructure’s robust
metadata/messaging header support) or the nature of the exchange itself
does not require any accompanying message data structures (perhaps due
to the exchange’s simplicity). In these situations, the use of FIXM Core
alone should be sufficient.

FIXM Core is the repository in which all globally applicable flight data
structures reside. The root field of the entire flight information
hierarchy is the Flight class (in the physical model, the Flight
element).

<img src=".//media/image50.emf" style="width:6.26806in;height:4.11389in" />

When using FIXM Core for data representation, all XML documents must
begin with this Flight element. Similarly, the Fixm.xsd schema file is
the root schema of FIXM Core. Whether validating FIXM Core XML documents
or using automated code generation utilities (such as JAXB), this is the
schema file that should be referenced.

*Example: Departure/Arrival Alerts*

Our fictitious user XAS begins their use of FIXM wanting to publish
departure and arrival alerts for flights they monitor. XAS sets up a
publishing service with which they send out arrival and departure
messages to a single endpoint their consumers can monitor to receive the
alerts. Due to the simplicity of their service, the use of FIXM Core
alone is sufficient for their needs. XAS constructs XML messages
starting with the Flight element to convey their data and instructs
their consumers to validate these messages against FIXM Core’s Fixm.xsd
schema file. Below is an example of how the XML payload of a departure
alert coming from this service may appear.

&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;fx:Flight xmlns:fx="http://www.fixm.aero/flight/4.2"
xmlns:fb="http://www.fixm.aero/base/4.2"&gt;

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

&lt;/fx:Flight&gt;

