## FIXM XML Structural Overview

The FIXM XML Schema, based on the FIXM Logical Model, arranges
information about flights in a different manner than the ATS message
format. While the ATS format emphasizes space (and therefore bandwidth)
savings, the FIXM format emphasizes structure and clarity. Here is a
“skeleton” for a typical Flight Plan message. It does not show every
field that will be included in upcoming FF-ICE messages but shows many
of the common fields found in the ATS messages that have been converted
to FIXM format. Some messages, such as Departure and Arrival, do not
have route trajectory and aircraft information, for example, and are
therefore much more compact than messages containing full Flight Plan
data.

&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;mesg:Message xmlns:fb="http://www.fixm.aero/base/4.1"
xmlns:fx="http://www.fixm.aero/flight/4.1"
xmlns:mesg="http://www.fixm.aero/messaging/4.1"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
messageType="FPL"&gt;

&lt;!-- This message header area contains general information, such as
senders and receivers --&gt;

&lt;mesg:uniqueMessageIdentifier&gt;

&lt;!-- A universally unique identification (uuid) for this message
--&gt;

&lt;/mesg:uniqueMessageIdentifier&gt;/&gt;

&lt;mesg:flight&gt;

&lt;fx:aircraft&gt;

&lt;!-- Information such as aircraft type, registration and capabilities
appears here --&gt;

&lt;/fx:aircraft&gt;

&lt;fx:arrival&gt;

&lt;!-- Destination aerodrome and alternates appear here. In the case of
an arrival message, arrival time and aerodrome also appear --&gt;

&lt;/fx:arrival&gt;

&lt;fx:departure&gt;

&lt;!-- Departure aerodrome, alternates, and estimated off-block time go
here --&gt;

&lt;/fx:departure&gt;

&lt;fx:filed&gt;

&lt;!-- The route trajectory for the flight is shown here. It can
contain climb and descent schedules and profiles, 0 to 2000 elements,
route information, and take-off weight --&gt;

&lt;fx:element&gt;

&lt;!-- Each element contains information pertinent to a single point in
the trajectory, such as distance, constraints, enroute delays, route
changes, name of the point this element represents, and the name (if
any) of the route along which the flight will proceed to the next
element --&gt;

&lt;/fx:element&gt;

&lt;fx:routeInformation&gt;

&lt;!-- Contains the route text where available, cruising level and
speed, estimated elapsed time. --&gt;

&lt;/fx:routeInformation&gt;

&lt;/fx:filed&gt;

&lt;fx:flightIdentification&gt;

&lt;!-- The aircraft ID/call sign/tail number by which this flight is
identified by air traffic services --&gt;

&lt;/fx:flightIdentification&gt;

&lt;fx:gufi&gt;

&lt;!-- Globally unique identifier for this flight which can be used to
correlated different transactions for this flight --&gt;

&lt;/fx:gufi&gt;

&lt;/mesg:flight&gt;

&lt;/mesg:Message&gt;

The sample messages were generated in three groups, described in the
following sections.

*Note: As of the publication date of this document, the specific
technical vision for the global FF-ICE/R1 implementation is still under
discussion by ICAO ATMRPP. While FIXM achieves global harmonisation of
the flight information exchanged by FF-ICE services, it is not yet
decided whether particular aspects related to FF-ICE services
implementation, such as Messaging, should be subject to global
harmonisation.*

*The samples below rely on the Messaging package of FIXM 4.1.0. This
package has been intentionally deprecated by [Change Request
28](https://ost.eurocontrol.int/sites/FIXM/Change%20Requests/Deprecating_the_Messaging_package.docx)
as a signal to FIXM implementers that its use is not necessarily
recommended for global use for the time being, considering the
uncertainties with regards to the desired level of standardization for
FF-ICE and the declared scope of FIXM as outlined in the FIXM Strategy
v1.1, chapter 3. Nevertheless, these samples represent a valid approach
for encoding FF-ICE/R1 and/or ATS messages with FIXM-based content.
Other message encodings having FIXM-based content satisfying the
requirements outlined in chapter 2.2 may equally qualify as a valid
usage of FIXM.*

