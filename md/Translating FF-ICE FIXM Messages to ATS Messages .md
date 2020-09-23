## Translating FF-ICE FIXM Messages to ATS Messages 

### Target audience

FIXM is not developed as a permanent alternative to the traditional ICAO
FPL 2012 format but covers the content of the legacy ATS Messages. This
chapter targets FIXM implementers who want to realise a conversion from
FF-ICE Messages to ATS message content.

### Overview

The transition from present day practices to FF-ICE operations is likely
to be somewhat protracted. This is a topic that is being pursued
actively by the ATMRPP \[ATMRPP-WG/24-WP/564\] \[16\], and is recognized
as a key issue in the System Wide Information Management (SWIM) concept
\[15\] \[ICAO Doc 10039\]. During that transition period, there will be
stakeholders who are able to send and receive flight plan information
employing FIXM, while others will employ ICAO ATS messages. In such a
hybrid environment, it is expected that a significant effort will be
expended translating between the FIXM format and the ATS message format.
It is critical for interoperability purposes, and to ensure meaning is
not lost in translation, that the conversion between FIXM and ATS
message content is precisely defined, and that all stakeholders employ
the same translation rules.

There is not a direct correspondence between ATS messages and FIXM,
though there is a close association. At the message level, the
association is with the FF-ICE messages described in section3.3.1. The
mapping from FF-ICE Messages to ATS messages focuses on the individual
ATS message fields (7, 8, etc.) rather than the messages themselves. In
general, the mapping is independent of the message type: regardless of
which ATS message field 7 appears in, the aircraft identification always
maps to the same FIXM element. In the cases where an ATS message field
item maps to different FIXM elements based on the message type (e.g.
field 13b is estimated off block time in a FPL, but actual take off time
in a DEP), that difference is made explicit in the mapping rule.

### ATS Message Content to FIXM Logical Model Map

#### Purpose & Scope

This chapter provides a mapping between the Flight Information Exchange
Model (FIXM) Logical Model v4.1.0 and International Civil Aviation
Organisation (ICAO) Air Traffic Services (ATS) message content as
defined in ICAO Doc 4444 \[PANS-ATM\] \[8\].

The mapping provides traceability from ATS message content to FIXM
ensuring complete coverage of ATS messages.

This chapter defines a mapping from ICAO Doc 4444 \[PANS-ATM\] ATS
message fields to FIXM logical model elements. The scope covers all
message content defined in appendix 3 of PANS-ATM \[8\]. Supporting
description is provided where the mapping from ATS message content to
the logical model is not clear. The reader is assumed to be familiar
with ICAO ATS messages and the FIXM Logical Model.

This chapter does not address the FIXM Extensible Markup Language (XML)
schemas. The mapping from the logical model to the XML schemas is
relatively straightforward.

#### Guidelines

Section **Error! Reference source not found.** maps the individual data
elements in ATS messages to the corresponding elements in the FIXM
logical model. It is not always clear how the structural aspects of an
ATS message are captured in a FIXM object. This section provides
explanation and guidelines where the structure is not clear.

The ATS message format consists of a mixture of structured and free
text. The free text components create problems when decoding ATS
messages, regardless of whether the goal is to create FIXM objects from
the ATS messages. The format of ATS messages is in part dictated by the
need for such messages to be readable by a human (presentation is a
concern), whereas FIXM focuses purely on the content and structure
(presentation is not a concern). Those free text aspects of ATS messages
that cause difficulties when decoding are highlighted and discussed.

##### Emergency Message Originator

ATS field 5b is the originator of the emergency message. It consists of
eight letters: location indicator (4), ATS unit designator (3), and
either ‘X’ or a letter identifying the ATS unit division.

It is only possible to create a valid ATS message field 5b from a FIXM
flight if the attribute atcUnitNameOrAlternate is eight upper case
letters.

##### SSR Mode

ATS field 7b is Secondary Surveillance Radar (SSR) mode. PANS-ATM
restricts this to mode A only. FIXM supports SSR code but does not
include explicitly a field for mode (that mode A alone is supported is
implicit in the class name: *ModeACode*).

When creating ATS message content from a FIXM object, set the SSR mode
(field 7b) to A.

##### Number of Aircraft

ATS field 9a is the number of aircraft. PANS-ATM restricts this value to
be in the range 2 through 99. FIXM allows any non-negative number.

When creating ATS message content from a FIXM object, if the
Aircraft.formationCount value is greater than 99, truncate to 99.

A similar comment applies to other ATS message fields that contain
counts:

-   Field 18 TYP (range 2..10);

-   Field 19b (range 1..99);

-   Field 19f (range 1..99 for number of dinghies, 1..999 for dinghy
    capacity).

##### Wake Turbulence Category

PANS-ATM supports wake turbulence categories L, M and H (field 9c).
However, aircraft operators who operate A380’s often specify a wake
turbulence category of J. FIXM supports the value J.

Since J is in common use, when creating a FIXM object from ATS message
content, if wake turbulence category J is specified, include that value
in the ATS message.

##### Navigation/Communication Capabilities

###### No or Unserviceable Equipment

The value ‘N’ in field 10a of an ATS messages indicates, “no
COM/NAV/approach aid equipment for the route to be flown is carried, or
the equipment is unserviceable”. FIXM does not explicitly model the
field 10a code ‘N’. Rather it leaves that code implicit to avoid
redundancy. The relevant items in the FIXM logical model are class
*FlightCapabilities* and its associations *navigation*, *communication*
and *standardCapabilities*.

-   When creating a FIXM object from ATS message content, ignore code
    ‘N’ in field 10a[11].

-   When creating ATS message content from a FIXM object, insert ‘N’ in
    field 10a if an instance of class *FlightCapabilities* is absent, or
    it is present and associations *navigation*, *communication* and
    *standardCapabilities* are all absent.

###### Standard Equipment

The value ‘S’ in field 10a of an ATS message indicates, “Standard
COM/NAV/approach aid equipment for the route to be flown is carried and
serviceable”. ‘S’ is not specific to navigation or communication
capabilities. As such, FIXM represents standard equipment and
capabilities via class *StandardCapabilitiesIndicator* that is
associated with *FlightCapabilities*, being the lowest level class that
sits above the navigation and communication capabilities in the class
hierarchy.

###### PBN Approved

The value ‘R’ in field 10a of an ATS message indicates performance based
navigation (PBN) capability codes are included in field 18 PBN. FIXM
does not explicitly model the field 10a code ‘R’. Rather it leaves that
code implicit to avoid redundancy.

-   When creating a FIXM object from ATS message content, ignore code
    ‘R’ in field 10a[12].

-   When creating ATS message content from a FIXM object, insert ‘R’ in
    field 10a if one or more PBN codes are present in the navigation
    capabilities.

###### Other Equipment and Capabilities

The value ‘Z’ in field 10a of an ATS message indicates that other
communication/navigation capabilities are defined in field 18 (NAV, COM,
DAT). FIXM does not explicitly model field 10a code ‘Z’. Rather, it
leaves that code implicit to avoid redundancy.

-   When creating a FIXM object from ATS message content, ignore code
    ‘Z’ in field 10a[13].

-   When creating ATS message content from a FIXM object, insert ‘Z’ in
    field 10a if at least one of the “other navigation, communication or
    datalink capabilities” fields is present in the FIXM object.

PANS-ATM states: *If the letter G is used, the types of external GNSS
augmentation, if any, are specified in item 18 following the indicator
NAV/*. An ATS message may have content in field 18 NAV/ with ‘G’ in
field 10a but not ‘Z’. The above rule always inserts ‘Z’ in field 10a if
there is content in field 18 NAV/. Consequently, an ATS-FIXM-ATS round
trip may insert a ‘Z’ in field 10a that was not in the original ATS
message.

###### Equipment/Capabilities Example

Figure 33 presents a flight plan in ICAO 4444 format, with equipment and
capabilities related to navigation and communication highlighted.

(FPL-QFA8-IS

-B744/H-SDE2E3FGHIJ3J5M1RWYZ/LB1D1

-KDFW0400

-N0501F280 DCT ABI J4 INK/N0504F300 J50 ELP J26 HMO V2 GRN

2704N11627W 26N119W 2544N12000W 24N126W/M084F320 22N133W 19N139W

16N144W/M084F340 11N152W 06N159W/M084F360 01N166W 01S169W

0500S17435W 06S176W 12S176E/M084F380 18S168E 2125S16300E GUXIB R587

HARVS Q21 SAVER G329 BN DCT

-YBBN1519

-PBN/A1B1D1L1S1 NAV/GPSRNAV RNVD1A1 DOF/130202 REG/VHOEG

DLE/INK0100 26N119W0200 SEL/MQDE

PER/D RIF/GUXIB R587 MEPAB G591 LTO NWWW)

<span id="_Ref262546549" class="anchor"></span>Figure 33: Sample Flight
Plan

Figure 34 presents the equipment/capabilities portion of the flight plan
as a FIXM object model. Only the highlighted items in Figure 33 are
included in the diagram.

<img src=".//media/image37.png" style="width:6.30208in;height:5.61458in" alt="NavCom" />

<span id="_Ref262546619" class="anchor"></span>Figure 34: Equipment and
Capabilities Object Model

##### Surveillance Capabilities

The value ‘N’ in field 10b of an ATS messages indicates, “no
surveillance equipment for the route to be flown is carried, or the
equipment is unserviceable”. FIXM does not explicitly model the field
10b code ‘N’. Rather it leaves that code implicit to avoid redundancy.
The relevant items in the FIXM logical model are class
*FlightCapabilities* and its association *surveillance*.

-   When creating a FIXM object from ATS message content, ignore code
    ‘N’ in field 10b[14].

-   When creating ATS message content from a FIXM object, insert ‘N’ in
    field 10b if an instance of class *FlightCapabilities* is absent, or
    it is present but no surveillance capability codes are present.

##### Date/Time/Duration Specification

###### UTC

Date/time values in ATS messages are always expressed in Coordinated
Universal Time (UTC). Likewise, FIXM requires times to be expressed in
UTC.

A constraint is placed on class *Base.Types.Time*, the class used to
represent all date/time values in FIXM, such that only UTC times can be
expressed. The constraint mandates that the time zone is ‘Z’.

Example: 20<sup>th</sup> July 1969 at 20:18UTC is expressed as

> 1969-07-20T20:18:00.000Z

In ATS messages, times are expressed in hours and minutes only, while
FIXM supports seconds and fractions of seconds. When converting FIXM to
ATS message content, seconds should be truncated.

###### Date of Flight

The flight departure time is encoded in field 13b of an ATS message, and
is expressed as a four digit UTC value (HHMM). The date on which the
flight departs optionally appears in field 18 DOF (YYMMDD). FIXM encodes
such values as a full date/time, not as distinct date and time values.
As such, the full and unambiguous departure date/time of a flight is
composed from fields 13b and 18 DOF[15].

Figure 35 presents the object model corresponding to highlighted parts
of the following flight plan fragment.

-YSSY2315

-N0501F280 ....

-YBBN0115

-DOF/141105

<img src=".//media/image38.png" style="width:3.19792in;height:1.09375in" alt="DOF" />

<span id="_Ref277922327" class="anchor"></span>Figure 35: Departure
Date/Time Object Model

###### Estimated Flight Time

ATS field 16b is the total estimated elapsed time from take-off to
landing, consisting of four digits in HHMM format. FIXM models this as a
duration which may be of arbitrary length. Consequently, a FIXM flight
may include a duration that is not expressible in an ATS message.

The same comments applies to other ATS message fields that contain
durations:

-   Field 18 EET;

-   Field 18 DLE;

-   Field 19a.

##### Route

An ATS message route description (field 15) is captured in FIXM by class
*RouteTrajectoryGroup* in package
*Flight.FlightRouteTrajectory.RouteTrajectory*.

The initial cruising speed (field 15a) and level (field 15b) are
captured in class *FlightRouteInformation*. Field 15b of an ATS route
may contain the token ‘VFR’ instead of a level. In that case the
*cruisingLevel* attribute of *FlightRouteInformation* should be omitted.

The route is modelled as a series of route elements (class
*RouteTrajectoryElement*) each consisting of a route point and the
designator of the ATS route to the next point, together with associated
information such as delay and changes.

Note this package also accommodates 4D trajectories hence is far richer
in content than is required for ATS message routes. When mapping from
ATS messages to FIXM there is no requirement to create a corresponding
4D trajectory.

###### Varieties of Route

The mapping from field 15 to FIXM is complicated by the fact that a FIXM
object, class *Flight*, can be associated with up to five routes or
trajectories to support FF-ICE processes. The associations are:

-   negotiating (exchange between eASP and eAU during the Planning
    Phase)

-   agreed (by the eASP and eAU during the Planning Phase)

-   filed (by the eAU)

-   current (latest known information)

-   desired (by the eAU)

When mapping ATS message content to FIXM it must be decided which of the
associations is employed to model the route information. Such a decision
cannot be made with respect to field 15 in isolation. The decision is
dependent on the message type in which the route occurs. Table 3
presents the mapping between kinds of route and the message types that
contain field 15 (including those where field 15 is incorporated in
field 22).

<span id="_Ref285513293" class="anchor"></span>Table 3: Messages Types
Supporting Field 15

| Message Type | Route Association |
|--------------|-------------------|
| ALR          | current           |
| FPL          | filed             |
| CHG          | filed             |
| CPL          | current           |
| CDN          | current           |

###### Route Text

The primary purpose of FIXM is to provide a structured representation of
flight information, with individual elements clearly delineated to
ensure the intent of the route is communicated unambiguously. The
attribute *routeText* in class *FlightRouteInformation* allows the text
of a route description, namely the content of field 15c in the ATS
message, to be recorded in the model. This is provided to support legacy
systems, and to support stakeholders who may not be in full possession
of all necessary aeronautical resource information. When translating
from field 15c of an ATS message to FIXM the route structure should be
decoded and made explicit.

-   When creating a FIXM object from ATS message content, whenever
    possible decode the route and populate the FIXM route structure.

-   When the FIXM route structure is populated, population of the route
    text is optional.

-   For legacy systems where it is not possible to decode the route, the
    route text only may be populated.

-   When the route text is populated, strip leading and trailing white
    space, and replace multiple contiguous white space characters by a
    single space.

-   When creating ATS message content from FIXM, if the route structure
    is available, create the field 15c text from the route structure
    (even if the route text is available).

-   Never populate the route text with anything other than a string that
    complies with the PANS-ATM field 15c route definition.

###### SID and STAR

A SID, if present in the route, is the first item in the route
description. A STAR, if present in the route, is the last item in the
route description. FIXM encodes the SID and STAR as route designators in
the route: attributes *standardInstrumentDeparture* and
*standardInstrumentArrival* in class
*RouteDesignatorToNextElementChoice*.

-   A SID, if included in a route, must appear in the first element of
    the sequence of instances of *RouteTrajectoryElement*. The
    *elementStartPoint* attribute of the same element must not be
    populated.

-   A STAR, if included in a route, must appear in the last element of
    the sequence of instances of *RouteTrajectoryElement*.

###### Direct Route Segments

In ICAO ATS messages, the presence of DCT between two route points
indicates the aircraft will fly between the points outside a designated
ATS route. In the ICAO ATS message it is also allowed to specify two
consecutive route points that are separated neither by an ATS route
designator nor by DCT; this is most commonly seen in User Preferred
Routes (UPR). In such a case there is an implied DCT between the route
points.

FIXM models DCT through class *OtherRouteDesignator*, related to class
*RouteDesignatorToNextElementChoice* by attribute otherRouteDesignator.

-   When creating a FIXM object from ATS message content, indicate a
    direct route segment by setting attribute *otherRouteDesaignator* to
    DIRECT.

-   When creating ATS message content from a FIXM object, if
    *otherRouteDesignator* of class *RouteDesignatorToNextElementChoice*
    is set to DIRECT, insert “DCT” into the ATS route.

-   When creating ATS message content from a FIXM object, if an instance
    of class *RouteDesignatorToNextElementChoice* is not present, or is
    present and the value of attribute *otherRouteDesignator* is
    UNSPECIFIED, do not insert any text between the current and next
    point.

Refer to Figure 37 for an example of “DCT” in a route.

###### Route Truncation

The token ‘T’ in a route description indicates the route has been
truncated. That is, the entire route through to the destination has not
been presented. When included, the route truncation indicator must be
the last item in the route description.

Route truncation is modelled by class *RouteTruncationIndicator* in
package *RouteTrajectory*, and is associated with class
*RouteTrajectoryElement*. A route is modelled by an ordered sequence of
instances of *RouteTrajectoryElement*. The truncation indicator may only
be associated with the last element in the sequence (it is meaningless
to truncate a route prior to the last element).

Refer to Figure 37 for an example of route truncation.

###### Route Changes

Route and trajectory information is captured in the FIXM logical model
in package *Flight.FlightRouteTrajectory*. The route itself is captured
in sub-package *RouteTrajectory*, while changes to speed and level in a
route are captured in sub-package *RouteChanges*.

This section defines how the route changes defined in PANS-ATM are
mapped to the FIXM logical model. There are three variants allowed in an
ATS message: speed/level change, cruise/climb, and cruise/climb with no
specific upper limit. One example of each of those changes and how they
map to the FIXM logical model is presented in Table 4.

<span id="_Ref457456350" class="anchor"></span>Table 4: Route Changes

<table>
<thead>
<tr class="header">
<th><strong>Example</strong></th>
<th><strong>Description</strong></th>
<th><strong>Modelled As</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N0430F300</td>
<td>Change TAS to 430 knots and request FL300.</td>
<td><p>CruisingSpeedChange</p>
<p>CrusingLevelChange</p></td>
</tr>
<tr class="even">
<td>N0430F300F320</td>
<td>Change TAS to 430 knots and request climb from FL300 to FL320.</td>
<td>CruiseClimbStart (with level/altitude range)</td>
</tr>
<tr class="odd">
<td>N0430F300PLUS</td>
<td>Change TAS to 430 knots and request climb commencing above FL300.</td>
<td>CruiseClimbStart (with single level/altitude)</td>
</tr>
</tbody>
</table>

Notes:

-   The token ‘C’ is inserted in a flight plan to indicate a cruise
    climb phase. This does not appear in the FIXM logical model. The
    presence of an instance of class *CruiseClimbStart* indicates cruise
    climb, as demonstrated in Figure 36.

-   The token ‘PLUS’ is used to indicate cruise climb is planned to
    commence above the specified level. This does not appear in the FIXM
    logical model. ‘PLUS’ is indicated by an instance of
    *CruiseClimbStart* where *level* (of class
    *FlightLevelOrAltitudeOrRangeChoice*) is populated with an instance
    of FlightLevelOrAltitudeChoice), whereas a cruise/climb with an
    upper limit is indicated by an instance of *CruiseClimbStart* where
    *level* is populated with an instance of *VerticalRange*.

-   *CrusingSpeedChange* and *CruisingLevelChange* have an optional
    association *activation*. There is no necessity to populate this
    attribute.

Figure 36 presents examples of the three kinds of level constraint.

<img src=".//media/image39.png" style="width:6.26042in;height:3.83333in" alt="SPDLVL" />

<span id="_Ref456948489" class="anchor"></span>Figure 36: Route Changes
Object Model

Figure 37 presents the object model corresponding to the (contrived) ATS
message field 15 route

> N0430F220 GORLO2N 3910N02230W/N0415F240 DCT C/IVA/N0415F240F250 B9
> ENTRA VFR T

<img src=".//media/image40.png" style="width:6.26042in;height:7.59375in" alt="RTE" />

<span id="_Ref262546937" class="anchor"></span>Figure 37: Route Object
Model

###### RIF

ICAO field 18 RIF, if present, contains the route details to the revised
destination, followed by the revised destination aerodrome. This is
modelled in FIXM by class *ReclearanceInFlight* in package
*Flight.Arrival*. The route component is modelled by attribute
*routeToRevisedDestination* and the destination by attribute
*filedRevisedDestinationAerodrome*.

The route component is constructed via the same rules as for field 15c.
However, in FIXM the route to revised destination is modelled as an
unstructured string.

Figure 38 presents the object model corresponding to field 18 RIF of the
sample flight plan in Figure 33:

RIF/GUXIB R587 MEPAB G591 LTO NWWW

<img src=".//media/image41.png" style="width:3.30208in;height:1.20833in" alt="RIF" />

<span id="_Ref262547023" class="anchor"></span>Figure 38: Route to
Revised Destination Object Model

###### DLE

ICAO field 18 DLE, if present, contains points along the route at which
delay will occur; the aircraft essentially goes ‘off plan’ for the
stated duration. Each DLE point must appear in the route (field 15c).
For ATS messages, this requires that a consistency check be performed on
the flight plan to ensure the DLE points are listed in the route. FIXM
avoids the need for a check and the duplication of route points by
incorporating a delay value in the corresponding route element.
Specifically, the delay duration appears in attribute *delayValue* of
class *EnRouteDelay*, which is associated with class
*RouteTrajectoryElement*.

The *EnRouteDelay* class additionally has attributes *delayReason*,
*delayReference* and *delayType*. When creating a FIXM object from ATS
message content, the attributes *delayReason*, *delayReference* and
*delayType* should be omitted.

Figure 39 presents the object model for a fragment of the route in the
flight plan contained in Figure 33, incorporating the information in
field 18 DLE:

DLE/INK0100 26N119W0200

<img src=".//media/image42.png" style="width:6.26042in;height:4.51042in" alt="DLE" />

<span id="_Ref262549907" class="anchor"></span>Figure 39: Route Delay
Object Model

##### Aircraft Type

When the type of aircraft that conducts a flight does not have an ICAO
aircraft type designator \[ICAO Doc 8643\] \[12\] or the flight is a
formation, the value ZZZZ is inserted in field 9b and the aircraft type
information is inserted in field 18 TYP. The following fragment is an
example.

-10ZZZZ/M

....

-TYP/2F15 5F5 3B2

Note the structured nature of the TYP field: two F15s, five F5s, and
three B2s. The value in field 18 TYP may exhibit structure as in this
example above for a formation. However, this may not be so in other
cases, where the (non-designator) type of aircraft is listed, as in

-ZZZZ/L

....

-TYP/ECLIPSE 500

Figure 40 presents the object model corresponding to each of the above
flight plan fragments.

<img src=".//media/image43.png" style="width:6.30208in;height:3.51042in" alt="ATYP" />

<span id="_Ref265180403" class="anchor"></span>Figure 40: Aircraft Type
Object Model

Notes:

-   If it is not possible to decode the content of field 18 TYP, create
    a single instance of class *AircraftType* to record the entire
    content of 18 TYP.

-   The sum of the *numberOfAircraft* attributes in the instances of
    *AircraftType* class should equal the *formationCount* attribute in
    class *Aircraft*.

-   If the number of aircraft is 1, the *formationCount* and
    *numberOfAircraft* attributes may be omitted (though may be included
    as in Figure 40).

##### Aircraft Registration

The registration mark for an aircraft may include a ‘-’ character, e.g.
VH-ABC. While PANS-ATM does not explicitly state that ‘-’ should be
omitted when including field 18 REG, it is rare that ‘-’ is included,
i.e. VHABC is the norm. FIXM does not support ‘-’ in the registration.

When creating a FIXM object from an ATS message, strip the ‘-’ character
if present in the registration.

FIXM supports multiple registrations. ATS messages support a single
registration. When creating a FIXM object from an ATS message, the
registration is a sequence one length one.

When creating an ATS message from a FIXM object, if the FIXM object
contains multiple registrations, select the first registration in the
sequence.

##### Departure Aerodrome

When the departure aerodrome for a flight does not have an ICAO location
indicator code \[ICAO Doc 7910\] \[11\], the value ZZZZ is inserted in
field 13a and the departure point is inserted in field 18 DEP. According
to PANS-ATM the content of 18 DEP is “name and location of departure
aerodrome” where the location is expressed either as a
latitude/longitude or as a bearing and distance from a designated point.
In the case the aircraft did not take off from an aerodrome, the first
point of the route or the marker radio beacon may be specified. This can
be problematic when decoding 18 DEP for the population of FIXM:

-   Analysis of flight plans received by Airservices Australia shows
    that the majority of flight plans that include 18 DEP contain only a
    latitude/longitude in 18 DEP. This is, strictly speaking, not
    compliant with PANS-ATM, yet it is common practice.

-   The name of the departure aerodrome may consist of multiple words so
    it may not be obvious how to parse the content of 18 DEP.

Figure 41 presents two object models corresponding to the following
flight plan fragment.

-ZZZZ1231

....

-DEP/WESTMEAD HOSPITAL 3349S15059E

<img src=".//media/image44.png" style="width:4.33333in;height:4.70833in" alt="DEP" />

<span id="_Ref277670899" class="anchor"></span>Figure 41: Departure
Aerodrome Object Model

The first shows the fully decoded 18 DEP. The second shows the approach
where 18 DEP cannot be decoded successfully: insert the entire content
of 18 DEP in the *name* attribute of *AerodromeReference*.

##### Destination Aerodrome

When the destination aerodrome for a flight does not have an ICAO
location indicator code \[ICAO Doc 7910\] \[11\], the value ZZZZ is
inserted in field 16a and the destination point is inserted in field 18
DEST. According to PANS-ATM the content of 18 DEST is “name and location
of destination aerodrome” where the location is expressed either as a
latitude/longitude or as a bearing and distance from a named significant
point. This can be problematic when decoding 18 DEST for the population
of FIXM:

-   Analysis of flight plans received by Airservices Australia shows
    that the majority of flight plans that include 18 DEST contain only
    a latitude/longitude in 18 DEST. This is, strictly speaking, not
    compliant with PANS-ATM, yet it is common practice.

-   The name of the departure aerodrome may consist of multiple words so
    it may not be obvious how to parse the content of 18 DEST.

Refer to section Departure Aerodrome for an equivalent example in the
context of field 18 DEP.

##### Arrival Aerodrome

An ATS arrival message records the arrival aerodrome in field 17. If the
arrival aerodrome does not have an ICAO location indicator code, the
value ZZZZ is inserted in field 17a and the arrival aerodrome name is
recorded in field 17c.

FIXM accommodates both a destination (intended) aerodrome and an actual
arrival aerodrome.

-   Record the actual arrival aerodrome in attribute
    *arrivalAerodrome.locationIndicator* of class
    *Arrival.AerodromeReference*;

-   If the actual arrival aerodrome does not have an ICAO location
    indicator, record the arrival aerodrome name against attribute
    *arrivalAerodorme.name* of class *Arrival.AerodromeReference*.

Figure 42 presents an object model for destination/arrival information
assuming reception of the FPL

(FPL-RAQ-VG

-C172/L-V/C

-YBSU0540

-N0115A035 DCT

-YRED0021

-DOF/140622 REG/RAQ)

Followed by the ARR

(ARR-RAQ-YBSU-YRED-ZZZZ0622 CABOOLTURE)

<img src=".//media/image45.png" style="width:4.625in;height:2.48958in" alt="ARR" />

<span id="_Ref265076386" class="anchor"></span>Figure 42: Arrival
Aerodrome Object Model

##### Alternate Destination

When the alternate destination aerodrome for a flight does not have an
ICAO location indicator code \[ICAO Doc 7910\] \[11\], the value ZZZZ is
inserted in field 16c and the alternate destination point is inserted in
field 18 ALTN. Although similar to 18 DEP and 18 DEST there is an added
complication that up to two alternates may be specified, hence 18 ALTN
could include two name/location pairs.

The alternate destination aerodromes are captured by FIXM in attribute
*destinationAerodromeAlternate* of class *Arrival*.

The following flight plan fragment presents field 16 and field 18 items
that relate to destination aerodrome and alternates.

-ZZZZ0035 YSBK ZZZZ

……..

-DEST/WESTMEAD HOSPITAL 3348S15059E ALTN/EASTERN CREEK

Figure 43 presents the FIXM representation in an object model.

<img src=".//media/image46.png" style="width:5.79167in;height:4.6875in" alt="ALTN" />

<span id="_Ref262563475" class="anchor"></span>Figure 43: Destination
and Alternate Object Model

Decoding is problematic if two free text names are included in ALTN. For
example, consider the flight plan fragment

-YSBK0035 ZZZZ ZZZZ

……..

-ALTN/WESTMEAD HOSPITAL EASTERN CREEK

where “WESTMEAD HOSPITAL” and “EASTERN CREEK” are distinct points. None
of the tokens is a latitude/longitude or a bearing&distance, so it is
very difficult to distinguish them. In this case create a single
alternate location (instance of *AerodromeReference*) and set the *name*
attribute to “WESTMEAD HOSPITAL EASTERN CREEK”.

##### En-Route Alternate

ICAO field 18 RALT, if present, indicates the (one or more) en-route
alternates. Each alternate is one of:

-   ICAO location indicator;

-   Aerodrome name as listed in Aeronautical Information Publication
    (AIP);

-   Geographic location as a latitude/longitude;

-   Bearing and distance from a designated point.

An en-route alternate is represented in the model by attribute
*alternateAerodrome* of class *EnRoute* in package *Flight.EnRoute*.
Each alternate is an *AerodromeReference* (see section
AerodromeReference).

Figure 44 presents two object models that represent the en-route
alternate listed below.

RALT/YSBK WESTMEAD HOSPITAL SY102025

<img src=".//media/image47.png" style="width:5in;height:5.85417in" alt="RALT" />

<span id="_Ref265173251" class="anchor"></span>Figure 44: En-Route
Alternate Object Model

The first shows the fully decoded 18 RALT. The second shows the approach
where 18 RALT cannot be decoded successfully: insert the entire content
of 18 RALT in the *name* attribute of *AerodromeReference*.

##### Take-off Alternate

ICAO field 18 TALT, if present, indicates the (one or more) take-off
alternates. Each alternate is one of:

-   ICAO location indicator;

-   Aerodrome name as listed in AIP;

-   Geographic location as a latitude/longitude;

-   Bearing and distance from a designated point.

A take-off alternate is represented in the model by attribute
*takeOffAlternateAerodrome* of class *Departure* in package
*Flight.Departure*. Each alternate is an *AerodromeReference* (see
section AerodromeReference).

Refer to section En-Route Alternate for an equivalent example in the
context of en-route alternate.

##### Air Filed

When a flight plan is filed in the air, the value AFIL is inserted in
field 13a and the ATS unit from which supplementary flight plan
information can be obtained is specified in field 18 DEP. The mapping
employs the attribute *flightPlanSubmitter* of class *Flight* for this
purpose, though the name is not immediately suggestive of the purpose
for which it is being used. In this situation the following rules should
be applied:

-   Populate the *name* attribute of *PersonOrOrganization* (via
    attribute *flightPlanSubmitter*) with the content of field 18 DEP.

-   Populate the *airfileIndicator* of class *Departure* (with the
    constant value AIRFILE).

-   Populate the attribute *airfileRouteStartTime* of class
    *FlightRouteInformation* in package
    *Flight.FlightRouteTrajectory.RouteTrajectory* with the content of
    field 13b.

-   The departure aerodrome (*aerodrome*) and departure time
    (*estimatedOffBlockTime*) of class *Departure* are not populated.

Figure 45 presents the FIXM representation of the following air filed
flight plan (fragment) as an object model.

-AFIL1254

....

-DEP/YBBBZQZA

<img src=".//media/image48.png" style="width:6.27083in;height:1.98958in" alt="AFIL" />

<span id="_Ref268982502" class="anchor"></span>Figure 45: AFIL Object
Model

##### Remarks

The remarks item (RMK/) of field 18 of a flight plan maps to attribute
*remarks* of class *Flight*. The content of remarks should not include
the ‘RMK/’ label. That is, a flight plan containing

> RMK/TCAS II EQUIPPED

results in

> remarks = “TCAS II EQUIPPED”

The same is true of all field 18 items. The item label is not included
in the content; it is implied by the structure.

##### Supplementary Information

Supplementary information (field 19) contains additional information
about a flight that is not transmitted in the flight plan.

Field 19b is the number of persons on board. Appendix 2 of PANS-ATM
suggests ‘TBN’ is inserted in field 19b if the number of persons on
board is not known. Appendix 3 suggests field 19b is omitted if the
value is not known. FIXM does not allow a distinction between the
absence of field 19b and its presence with value ‘TBN’.

-   When converting ATS message content to FIXM, if field 19b is
    populated with ‘TBN’, omit the *personsOnBoard* attribute from the
    FIXM *SupplementaryData* object.

-   When converting a FIXM object to ATS message field 19, if the
    *personsOnBoard* attribute is absent, do not include any text for
    field 19b.

The above rule means an ATS-FIXM-ATS round trip would cause the text
‘P/TBN’ to be removed from the original ATS message.

Figure 46 presents the object model corresponding to the following field
19 example.

–E/0745 P/6 R/VE S/M J/L D/2 8 C YELLOW A/YELLOW RED TAIL N/145E C/SMITH

<img src=".//media/image49.png" style="width:6.28125in;height:6.5in" alt="SPL" />

<span id="_Ref277670947" class="anchor"></span>Figure 46: Supplementary
Information Object Model

##### Alerting Search and Rescue Information

Field 20 of an ATS message, alerting search and rescue information,
consists of eight items, each of which, if not known by the originator,
is replaced by ‘NIL’ or ‘NOT KNOWN’. The first five items are precisely
defined, but the final three are free text fields, which leads to
difficulties when decoding.

It is beyond the scope of this chapter to address such a decoding issue.

##### Radio Failure Information

Field 21 of an ATS message, radio failure information, consists of six
items, each of which, if not known by the originator, is replaced by
‘NIL’ or ‘NOT KNOWN’. The first four items are precisely defined, but
the final two are free text fields, which leads to difficulties when
decoding.

It is beyond the scope of this chapter to address such a decoding issue.

#### Base Constructs

The ATS messages to FIXM logical model map in section 4.4.4 at times
maps an ATS message field to a structured FIXM entity without providing
further detail. This occurs with ‘lower level’ entities that are defined
in the FIXM *Base* package. One such example is field 15a, which is
mapped to the *Base* class *TrueAirspeed*.

This section provides further detail for the mapping to *Base* classes
where those classes represent compound values.

##### FlightLevelOrAltitude

A level or altitude is captured in FIXM by the class
*FlightLevelOrAltitudeChoice* in package *Base.RangesAndChoices*. It
consists of choice between flight level (class *FlightLevel*) or
altitude (class *Altitude*). In each case a unit of measure is specified
(respectively *UomFlightLevel* and *UomAltitude*) and a vertical
distance (class *VerticalDistance* in package *Base.Measures*) expressed
as a floating point number. Table 5 provides a mapping between the
level/altitude in PANS-ATM ATS messages and the level/altitude in FIXM.

<span id="_Ref262563709" class="anchor"></span>Table 5: Level/Altitude
Mapping

| **ATS Message** | **FIXM**                     |                       |       |                       |
|-----------------|------------------------------|-----------------------|-------|-----------------------|
| Type            | Value                        | FlightLevelOrAltitude | *Uom* | Value                 |
| F               | Imperial flight level        | FlightLevel           | FL    | Imperial flight level |
| S               | Metric flight level          |                       | SM    | Metric flight level   |
| A               | Altitude in hundreds of feet | Altitude              | FT    | Altitude in feet      |
| M               | Altitude in tens of metres   |                       | M     | Altitude in metres    |

Notes:

-   For ICAO flight level type ‘F’, the ICAO and FIXM values are the
    same (though the ICAO value is a whole number while the FIXM value
    is a floating point number).

-   For ICAO flight level type ‘S’, the ICAO and FIXM values are the
    same (though the ICAO value is a whole number while the FIXM value
    is a floating point number).

-   For ICAO altitude type ‘A’, multiply by 100 when converting to FIXM.

-   For ICAO altitude type ‘A’, divide by 100 and round when converting
    from FIXM.

-   For ICAO altitude type ‘M’, multiply by 10 when converting to FIXM.

-   For ICAO altitude type ‘M’, divide by 10 and round when converting
    from FIXM.

-   Since rounding is necessary when converting from FIXM, a round trip
    transformation is not guaranteed to fully preserve meaning. For
    example, the FIXM altitude ‘2640 feet’ becomes ‘A026’ in which if
    converted back to FIXM becomes ‘2600 feet’.

##### TrueAirspeed

In ATS messaging speed is either true air speed or Mach number. This is
captured by class *TrueAirspeed* in package *Base.Measures*. It consists
of the unit of measurement (class *UomAirspeed*) and a (floating point)
value. Table 6 provides a mapping between the speed in ATS messages and
the speed in FIXM.

<span id="_Ref262563928" class="anchor"></span>Table 6: Speed Mapping

| **ATS Message** | **FIXM**                  |             |                         |
|-----------------|---------------------------|-------------|-------------------------|
| Type            | Value                     | UomAirspeed | Value                   |
| K               | Kilometres per hour       | KM\_H       | Kilometres per hour     |
| N               | Nautical miles per hour   | KT          | Nautical miles per hour |
| M               | Hundredths of Mach number | MACH        | Mach number             |

Notes:

-   In an ATS message the Mach value is represented by a three-digit
    string, which when interpreted as a number is 100 times greater than
    the Mach value (e.g. M080 is Mach 0.8).

-   Converting from FIXM to ATS message, multiply by 100 and round.

-   Converting from ATS message to FIXM, divide by 100.

-   Since rounding is necessary when converting from FIXM, a round trip
    transformation is not guaranteed to preserve meaning. For example,
    the FIXM Mach value of ‘0.841’ becomes ‘M084’ which when converted
    back to FIXM becomes ‘0.84’.

##### GeographicalPosition

In ATS messages, a geographic location is defined either in full
degrees, with a corresponding direct representation in decimal degrees,
or in degrees and minutes

> dd<sub>1</sub>mm<sub>1</sub>\[NS\]ddd<sub>2</sub>mm<sub>2</sub>\[EW\]

which is converted by

> decimal latitude = dd<sub>1</sub> + (mm<sub>1</sub>/60)
>
> decimal longitude = ddd<sub>2</sub> + (mm<sub>2</sub>/60)

When converting from FIXM to ATS messages, the position can only be
represented to the nearest minute, resulting in a loss of precision.

A round trip starting from FIXM may not preserve meaning. Example:

> FIXM latitude: 12.42 degrees
>
> Convert to ATS: 1225N (12 degrees, 25 minutes)
>
> Convert back to FIXM: 12.4166… degrees

##### SignificantPoint

A significant point can be a designated point (navaid or waypoint), a
geographic location (latitude/longitude), or a relative point (bearing
and distance from a designated point). Three subclasses of
*SignificantPoint* (which is abstract) capture the options:

-   Class *DesignatedPointOrNavaid* models the designator value via
    attribute *designator* of class *SignificantPointDesignator*.

-   Class *RelativePoint* models the relative point via attributes
    *referencePoint* (a *DesignatedPointOrNavaid*), *bearing* and
    *distance*.

-   Class *PositionPoint* models the point via attribute *position* of
    class *GeographicalPosition* (section GeographicalPosition).

Examples of significant points are presented in Figure 41 and Figure 44.

##### Frequency

Radio frequency can appear in fields 20d and 21b of an ATS message. In
all examples in PANS-ATM this is presented as an unadorned decimal
number (e.g. 126.7). The expanded text in PANS-ATM describing the
examples always states MHz.

The global guidance for ATC Interfacility Data Communications (AIDC)
\[PAN AIDC ICD\] \[14\] is more specific as presented in Table 7.

<span id="_Ref456782567" class="anchor"></span>Table 7: PAN AIDC ICD
Frequency

|     | **Range**          | **Units** |
|-----|--------------------|-----------|
| HF  | 2850 to 28000      | kHz       |
| VHF | 117.975 to 137.000 | MHz       |
| UHF | 225.000 to 399.975 | MHz       |

The mapping for ATS messages follows the PAN AIDC ICD convention.

FIXM captures radio frequency in class *Frequency* of package
*Base.Measures*. This class has a mandatory associated value: the unit
of measure (class *UomFrequency*). The frequency unit is either KHZ or
MHZ. If the frequency is four or five digits without a decimal point,
set the *uom* attribute to KHZ, otherwise set the *uom* attribute to
MHZ.


FIXM provides globally harmonized flight data definitions and a
standardized, hierarchical organization for representing information
about a flight. Though its main requirements driver is currently ICAO
FF-ICE, FIXM is intended as a general standard for representing all
flight data, and the use of FIXM is encouraged for any situation in
which flight data is exchanged between systems. Providing flight data in
FIXM format has the additional benefit of allowing the data to be more
easily ingested by any system already set up to process other FIXM
feeds. Essentially, the more FIXM is used, the more useful it becomes.

To help illustrate the use of FIXM outside of FF-ICE, this chapter
imagines a fictitious FIXM user, Example Air Services (XAS), that
expands their use of FIXM through increasingly complex use cases. Each
section below includes a high-level example of how the user accomplishes
their goals using the type of FIXM product described in the section.
When appropriate, these use cases are paired with the step-by-step
examples of how to build various FIXM products provided in the
Appendices at the end of this document.

