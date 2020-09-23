## General encoding rules

### Date/Time Specification

FIXM requires times to be expressed in UTC.

A constraint is placed on class *Base.Types.Time*, the class used to
represent all date/time values in FIXM, imposes the use of the trailing
character ‘z’ to indicate UTC, in line with the W3C XSD specification.

Example: 20th July 1969 at 20:18UTC is expressed as  
1969-07-20T20:18:00.000Z

**Note to implementers**

The mapping of the XSD type dateTime to native structures in various
development contexts is not always 1-1 and may exhibit a wide variety of
difficulties depending on the tooling and runtime context. In
particular, the trailing character ‘z’ indicating UTC may actually be
stripped/omitted, leading to FIXM times being interpreted as local times
instead of UTC times by some applications. FIXM implementers are
therefore invited to crosscheck that their systems correctly interpret
FIXM times as UTC time.

### Geographical positions

FIXM captures the concept of Geographical Position as defined by ICAO
Annex 15.

*Position (geographical). Set of coordinates (latitude and longitude)
referenced to the mathematical reference ellipsoid which define the
position of a point on the surface of the Earth.*

This model element maps to the ISO 19107 “Point” construct, defined as a
single location given by a direct position.

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image12.png" style="width:2.88042in;height:1.1381in" /></p>
<p><em>UML Class <strong>GeographicalPosition</strong> in package FIXM.Base.</em>AeronauticalReference</p></td>
<td><p>&lt;xs:complexType name="GeographicalPositionType"&gt;</p>
<p>&lt;xs:sequence&gt;</p>
<p>&lt;xs:element name="extension" type="fb:GeographicalPositionExtensionType" nillable="true" minOccurs="0" maxOccurs="2000"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="pos" type="fb:LatLongPosType" minOccurs="1" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;/xs:sequence&gt;</p>
<p>&lt;xs:attribute name="srsName" type="xs:string" use="required" fixed="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:complexType&gt;<br />
<em>Complex type <strong>GeographicalPositionType</strong> in file<br />
AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

A geographic location consists of a co-ordinate reference system and
geographic co-ordinates.

Co-ordinate reference system

ICAO Annex 11 chapter 2.29.1 states that World Geodetic System — 1984
(WGS-84) shall be used as the horizontal (geodetic) reference system for
air navigation. The Coordinate Reference System reference is critical
for the correct encoding and processing of FIXM positions*. This is
because a CRS not only indicates the geodetic datum and ellipsoid for
which point coordinates are expressed but also the order of the
coordinate axes in which coordinate values are provided, e.g. latitude
before longitude – which is an important convention for the aviation
domain.* \[copied from [OGC
12-028r1](https://portal.opengeospatial.org/files/?artifact_id=62061)\]
The EPSG:4326 CRS is the recommended choice for AIXM 5.1 data sets that
use the WGS-84 reference datum.

FIXM implements a fixed co-ordinate reference system:
“urn:ogc:def:crs:EPSG::4326”.

Geographic co-ordinates

The EPSG:4326 CRS has latitude as the primary axis, which indicates that
**the order of the values in the fb:pos element is** **first latitude**,
**second longitude**. This ordering convention is the one applied to the
aviation domain.

The co-ordinates are represented in FIXM by a two-valued sequence[4],
the first being the latitude and the second being the longitude, each of
which is a floating point number (the decimal value in degrees). The
direction is determined by the sign of the value, as specified in the
next table.

| Sign     | Latitude | Longitude |
|----------|----------|-----------|
| Positive | N        | E         |
| Negative | S        | W         |

Note the latitude and longitude values are encoded as double in FIXM.
Imposition of range restriction (-90≤latitude≤90, -180≤longitude≤180)
does not appear in the model since different elements of the sequence of
values have different constraints.

Examples

<img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />

<img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />

On EXAMPLE 1 above, number ‘59.0’ represents the latitude and number
‘-30.0’ represents the longitude.

Miscellaneous

The W3C XML schema 1.0 specification defines three special values for
float/double: positive infinity, negative infinity and not-a-number. In
this context, a “pos” element expressed as &lt;fb:pos&gt;INF
-INF&lt;/fb:pos&gt; or &lt;fb:pos&gt;NaN NaN&lt;/fb:pos&gt; would be
syntactically correct; it would validate against the core FIXM XML
schemas. However, it would not represent any plausible location. The use
of these special values is therefore not accepted when exchanging
geographical positions in FIXM.

Why FIXM does not use the Geography Markup Language (GML)

FIXM does not adopt the GML standard for the representation of
geospatial data. The reasons for not adopting GML are the following:

-   Wherever a GML dependency is introduced, there would be a need for
    users to use the GML schemas and therefore to understand GML, which
    increases implementation costs.

-   The Flight Planning community is not traditionally familiar with
    geospatial concepts. The introduction of GML would become an
    important drawback for FIXM adoption in support of FF-ICE/R1.

-   Introducing a dependency on GML would make FIXM more difficult to
    implement particularly in certain environments. For instance, .NET
    technologies have been identified as *incompatible* with the GML
    usage.

### References to published aeronautical information

Describing the predicted movement of a flight commonly means indicating
which parts of the infrastructure (ATS routes, waypoints, radio
navigation aids etc.) are expected to be used by the flight. This is
enabled in FIXM by a set of “references” constructs. These references
are not flight-specific information; they pertain to the aeronautical
information domain.

Different formats exist for exchanging aeronautical information, whose
usages depend on specific implementation considerations and actual
context within the overall data chain. For instance:

-   AIXM is developed in order to enable the provision in digital format
    of the aeronautical information that is in the scope of Aeronautical
    Information Services (AIS). AIXM 5.1 covers both the content of
    Aeronautical Information Publications (AIP) and of the NOTAM
    information.

-   The ARINC 424 standard defines a format for navigation (and
    communication) information, including but not limited to, aerodrome,
    runway, navaid, airway and terminal approach procedure information
    that is exchanged between data suppliers and avionics vendors.

-   The Aerodrome Mapping Exchange Schema (AMXM XML Schema) is an
    exchange format specification for AMDB as standardized by and
    dedicated to the EUROCAE/RTCA Aeronautical Databases WG44/SC217. It
    is an XML Schema implementation of the DO-291C/ED-119C AMXM UML
    model.

**FIXM does not import any of these formats or profiles thereof.** FIXM
defines its own structures for referring to aeronautical information
that are **self-contained** but mappable to their AIXM/AMXM… equivalents
thanks to the reuse of a common semantics. FIXM also provides an
**optional** mechanism enabling these self-contained references to be
supplemented with, but not replaced by, **hypertext** **references** to
AIXM features.

The following sections provide guidance for correctly encoding these
references in FIXM.

#### Generic hypertext references

If an AIXM 5.1 feature exists that corresponds to the element being
referred to, an **optional** hypertext reference to that AIXM feature
may be provided. This reference shall be expressed in accordance with
chapter 3.4.1 (*Abstract references using UUID*) of the [AIXM feature
Identification and
Reference](http://www.aixm.aero/sites/aixm.aero/files/imce/AIXM51/aixm_feature_identification_and_reference-1.0.pdf)
document developed by the AIXM community.

This hypertext reference may be used - or ignored - by the receiving
system depending on its capabilities.

Example:

> &lt;fx:*\[FIXMelement\]*
> href="urn:uuid:81e47548-9f00-4970-b641-8ff8f99098a5"&gt;

Important note: FIXM does not import the W3C XML Linking Language
(xlink) v1.1 schemas in order to represent the hypertext references.
FIXM mimics the xlink Locator attribute named “href” but defines it
within the FIXM (Base) namespace[5].

#### References to Waypoints

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image13.png" style="width:2.37391in;height:2.98811in" /></p>
<p><em>UML Class <strong>DesignatedPoint</strong> in package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:complexType name="DesignatedPointType"&gt;</p>
<p>&lt;xs:sequence&gt;</p>
<p>&lt;xs:element name="designator" type="fb:DesignatedPointDesignatorType" minOccurs="1" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="extension" type="fb:DesignatedPointExtensionType" nillable="true" minOccurs="0" maxOccurs="2000"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="position" type="fb:GeographicalPositionType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;/xs:sequence&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Complex type <strong>DesignatedPointType</strong> in<br />
file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

As a minimum, the coded designator of waypoint shall be provided, as
published in the AIPs.

OPTION 2 - Unambiguous reference

*(OPTION 2 = OPTION 1 + supplementary position information)*

The coded designator of a waypoint is not always sufficient for
unambiguously referring to that element. The 5-letter coded designator
of a waypoint is supposed to be unique world-wide (according to ICAO
Annex 11) but is not in reality. There are at least 5%
duplicates/triplicates/even more…

FIXM adds an optional property 'position' which may be used as a
complement to the 'designator' information in order to remove any
ambiguity on the designator.

Important note: the combinations of fields \[designator + position\]
shall not be interpreted as a natural key uniquely identifying the
waypoint, in so far as producing and consuming systems/services may use
different aeronautical information sources with different degree of
precisions for lat/long, leading to small variations of the position
information. The supplementary fields shall be used for disambiguation
purposes only (i.e. plausibility checks based on position) in case of
duplicate/triplicate/…

OPTION 3 - Minimum reference with supplementary AIXM pointer

*(OPTION 3 = OPTION 1 + supplementary hypertext reference)*

Option 3 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

OPTION 4 - Complete reference

*(OPTION 4 = OPTION 2 + OPTION 3)*

Option 4 corresponds to the combination of Option 2 and Option 3. See
explanations above.

Examples (NOT for OPERATIONAL USE)

The table below depicts examples of FIXM references to fictitious
Waypoint “TEMPO” that is ‘published’ in AIXM 5.1 as part of the
fictitious [Donlon
dataset](https://github.com/aixm/donlon/blob/master/Donlon.xml). The
data is entirely fictitious, located somewhere in the middle of the
Atlantic Ocean. The examples shall NEVER BE USED AS OPERATIONAL DATA.

<img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of Waypoint references in FIXM</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>OPTION 1</strong></p>
<p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />designator</p></td>
<td><p>&lt;fb:designatedPoint&gt;</p>
<p>&lt;fb:designator&gt;TEMPO&lt;/fb:designator&gt;</p>
<p>&lt;/fb:designatedPoint&gt;</p></td>
<td>This is the minimum reference that SHALL be provided.</td>
</tr>
<tr class="even">
<td><p><strong>OPTION 2</strong></p>
<p>designator<br />
+position</p></td>
<td><p>&lt;fb:designatedPoint&gt;</p>
<p>&lt;fb:designator&gt;TEMPO&lt;/fb:designator&gt;</p>
<p>&lt;fb:position srsName="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;fb:pos&gt;56.84 -29.860000000000003&lt;/fb:pos&gt;</p>
<p>&lt;/fb:position&gt;</p>
<p>&lt;/fb:designatedPoint&gt;</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>OPTION 3</strong></p>
<p>designator<br />
+href</p></td>
<td><p>&lt;fb:designatedPoint href="urn:uuid:81e47548-9f00-4970-b641-8ff8f99098a5"&gt;</p>
<p>&lt;fb:designator&gt;TEMPO&lt;/fb:designator&gt;</p>
<p>&lt;/fb:designatedPoint&gt;</p></td>
<td>Hypertext reference to be provided in accordance with the <a href="http://www.aixm.aero/sites/aixm.aero/files/imce/AIXM51/aixm_feature_identification_and_reference-1.0.pdf"><em>AIXM feature Identification and Reference document</em></a>, chapter 3.4.1.</td>
</tr>
<tr class="even">
<td><p><strong>OPTION 4</strong></p>
<p>designator<br />
+position<br />
+href</p></td>
<td><p>&lt;fb:designatedPoint href="urn:uuid:81e47548-9f00-4970-b641-8ff8f99098a5"&gt;</p>
<p>&lt;fb:designator&gt;TEMPO&lt;/fb:designator&gt;</p>
<p>&lt;fb:position srsName="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;fb:pos&gt;56.84 -29.860000000000003&lt;/fb:pos&gt;</p>
<p>&lt;/fb:position&gt;</p>
<p>&lt;/fb:designatedPoint&gt;</p></td>
<td></td>
</tr>
</tbody>
</table>

Note about the pattern constraint for waypoint designators

FIXM supports waypoint designators of 1 to 5 characters. This design is
intentional. In most cases, waypoints have a 5-letter designator, as
prescribed by ICAO. However, these designators might be shorter in some
particular cases. Examples of shorter waypoint designators could be
found in various sources:

-   In chapter 7 of the ARINC 424 specification. This chapter provides
    rules for forming the designators of waypoints in the absence of
    published designators. These rules can lead to designators of less
    than 5 characters. The following extracts from ARINC 424-19 provide
    some examples, which are highlighted in blue.

-   In the [US FAA’s publication of Instrument Flight Procedures
    encodings in ARINC 424-18
    format](https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/cifp/download/).
    For instance:

    -   Localizer only approach on RWY06 at KFOD

> SUSAP KFODK3FL06 AFOD 010FOD K3D 0V IF 18000 0 NS 854081209
>
> SUSAP KFODK3FL06 AFOD 020FF06 K3PC0E TF + 02800 0 NS 854091209
>
> SUSAP KFODK3FL06 AFOD 030FF06 K3PC0EE AR PI IFODK3 2430006119800100PI
> + 02800 0 NS 854101209
>
> SUSAP KFODK3FL06 AHIMSU 010HIMSUK3PC0E A IF FOD K3 15000140 D 18000 0
> NS 854111310
>
> SUSAP KFODK3FL06 AHIMSU 020SHRLAK3PC0EE BR AF FOD K3 216501401500 D +
> 02800 0 NS 854121310
>
> SUSAP KFODK3FL06 ALESFI 010LESFIK3PC0E A IF FOD K3 25400140 D 18000 0
> NS 854131310
>
> SUSAP KFODK3FL06 ALESFI 020SHRLAK3PC0EE BL AF FOD K3 216501402540 D +
> 02800 0 NS 854141310
>
> SUSAP KFODK3FL06 L 010SHRLAK3PC0E I IF IFODK3 24300163 PI + 02800
> 18000 0 NS 854151310
>
> SUSAP KFODK3FL06 L 020FF06 K3PC0E F CF IFODK3 2430006106300101PI +
> 02800 FO K3PN0 NS 854161209
>
> SUSAP KFODK3FL06 L 021ATLOJK3PC0E S CF IFODK3 2430003406300028PI +
> 01820 -324 0 NS 854171310
>
> SUSAP KFODK3FL06 L 030RW06 K3PG0GY M CF IFODK3 2430001306300021PI
> 01134 -324 0 NS 854181209
>
> SUSAP KFODK3FL06 L 040 0 M CA 0630 + 02800 0 NS 854191209
>
> SUSAP KFODK3FL06 L 050FOD K3D 0VY L DF + 02800 0 NS 854201209
>
> SUSAP KFODK3FL06 L 060FOD K3D 0VE R HM 1204T010 + 02800 0 NS 854211209

-   GPS approach on RWY29 at KFOT

> SUSAP KFOTK2FP29 ADINSE 010DINSEK2EA0E A IF 18000 P PS 857251211
>
> SUSAP KFOTK2FP29 ADINSE 020JEWPEK2PC0E TF + 06000 P PS 857261310
>
> SUSAP KFOTK2FP29 ADINSE 030SPHERK2PC0EE TF + 04700 P PS 857271310
>
> SUSAP KFOTK2FP29 AKNEES 010KNEESK2EA0E IF 18000 P PS 857281211
>
> SUSAP KFOTK2FP29 AKNEES 020YAGERK2EA0E A TF + 06800 P PS 857291211
>
> SUSAP KFOTK2FP29 AKNEES 030SPHERK2PC0EE TF + 04700 P PS 857301310
>
> SUSAP KFOTK2FP29 APLYAT 010PLYATK2EA0E A IF 18000 P PS 857311211
>
> SUSAP KFOTK2FP29 APLYAT 020JEVGYK2PC0E TF + 06000 P PS 857321310
>
> SUSAP KFOTK2FP29 APLYAT 030SPHERK2PC0EE TF + 04700 P PS 857331310
>
> SUSAP KFOTK2FP29 P 010SPHERK2PC0E I IF + 04700 18000 P PS 857341310
>
> SUSAP KFOTK2FP29 P 011JEVSYK2PC0E S TF + 03700 P PS 857351310
>
> SUSAP KFOTK2FP29 P 020ELLYSK2PC0E F TF + 02700 IZPUH K2PCP PS
> 857361310
>
> SUSAP KFOTK2FP29 P 021SP29 K2PC0E A TF + 01840 -356 P PS 857371211
>
> SUSAP KFOTK2FP29 P 030IZPUHK2PC0EY M TF 00617 -356 P PS 857381310
>
> SUSAP KFOTK2FP29 P 040 0 M CA 2757 + 01500 P PS 857391211
>
> SUSAP KFOTK2FP29 P 050FOT K2D 0VY R DF + 03000 P PS 857401211
>
> SUSAP KFOTK2FP29 P 060FOT K2D 0VE R HM 1610T010 + 03000 P PS 857411510

-   In the European AIS Database (EAD). A query on the EAD helped
    identify the following:

    -   40 occurrences of designated points with a 1-letter designator

    -   190 occurrences of designated points with a 2-letters designator

    -   356 occurrences of designated points with a 3-letters designator

    -   3046 occurrences of designated points with a 4-letters
        designator

> Most of the designated points with 2, 3 or 4-letter designators
> actually correspond to designated points formed after the position of
> a navaid or an aerodrome. However, some occurrences cannot be related
> to these cases. The following table quotes a few random examples.

| **Designator**        | **Lat**      | **Long**      | **Type** |
|-----------------------|--------------|---------------|----------|
| *1-letter designator* |              |               |          |
| N                     | 503241N      | 0042718E      | ADHP     |
| E                     | 502941N      | 0044206E      | ADHP     |
| A                     | 475826.0000N | 0161445.0000E | OTHER    |
| B                     | 475202.0000N | 0161514.0000E | OTHER    |
| B                     | 475734.0000N | 0161614.0000E | OTHER    |
| *2-letter designator* |              |               |          |
| S1                    | 460217N      | 0142702E      | OTHER    |
| S2                    | 460552N      | 0142748E      | OTHER    |
| S3                    | 460845N      | 0142452E      | OTHER    |
| W1                    | 461846N      | 0141449E      | OTHER    |
| W2                    | 461744N      | 0142049E      | OTHER    |
| A1                    | 453243N      | 0181709E      | OTHER    |
| A2                    | 423842N      | 0175651E      | ADHP     |
| A3                    | 434049N      | 0155502E      | ADHP     |
| *3-letter designator* |              |               |          |
| PJ1                   | 544005N      | 0253057E      | OTHER    |
| PJ2                   | 554243N      | 0211434E      | OTHER    |
| PJ3                   | 561350N      | 0221534E      | OTHER    |
| TP1                   | 481018.5959N | 0113540.1135E | ADHP     |
| TP2                   | 481314.6479N | 0113003.5398E | ADHP     |
| 13A                   | 512900.0000N | 0185100.0000E | OTHER    |
| 17A                   | 520800.0000N | 0174500.0000E | OTHER    |
| 20A                   | 514400.0000N | 0160800.0000E | OTHER    |
| 21A                   | 521300.0000N | 0162800.0000E | OTHER    |
| 27A                   | 523500.0000N | 0160500.0000E | OTHER    |
| ME1                   | 462338N      | 0155433E      | OTHER    |
| ME2                   | 463440N      | 0155009E      | OTHER    |
| DX1                   | 481323.7979N | 0122604.5443E | ADHP     |
| DX1                   | 505951.6149N | 0141519.3372E | ADHP     |
| DX2                   | 505625.7259N | 0141418.8105E | ADHP     |
| *4-letter designator* |              |               |          |
| SJ91                  | 000224S      | 1044205E      | OTHER    |
| FF36                  | 375713.7253S | 1751802.2481E | ADHP     |
| SM01                  | 464002.55N   | 0170535.52E   | ADHP     |
| SM02                  | 464750.28N   | 0165926.87E   | ADHP     |
| LDD5                  | 514138.7284N | 0191615.9435E | ADHP     |
| PG23                  | 545132N      | 0230742E      | OTHER    |
| IF09                  | 431021.1N    | 0252819.1E    | ADHP     |
| MAPT                  | 492818.3679N | 0083229.2734E | ADHP     |
| SDF2                  | 495218.7277N | 0112216.9347E | ADHP     |
| FF16                  | 513503.7055N | 1124320.1363W | ADHP     |
| ECHO                  | 504818N      | 0051950E      | ADHP     |
| ECHO                  | 482129.75N   | 0703422.93W   | OTHER    |

#### References to Navaid

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src=".//media/image14.png" style="width:2.33913in;height:2.82482in" /><br />
<em>UML Class <strong>Navaid</strong> in package FIXM.Base. AeronauticalReference</em></td>
<td><p>&lt;xs:complexType name="NavaidType"&gt;</p>
<p>&lt;xs:sequence&gt;</p>
<p>&lt;xs:element name="designator" type="fb:NavaidDesignatorType" minOccurs="1" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="extension" type="fb:NavaidExtensionType" nillable="true" minOccurs="0" maxOccurs="2000"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="navaidServiceType" type="fb:NavaidServiceTypeType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="position" type="fb:GeographicalPositionType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;/xs:sequence&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Complex type <strong>NavaidType</strong> in<br />
file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

As a minimum, the coded designator of a navaid shall be provided, as
published in the AIPs.

OPTION 2 - Unambiguous reference

*(OPTION 2 = OPTION 1 + supplementary position & navaidServicetype
information)*

The coded designator of a navaid is not always sufficient for
unambiguously referring to that element. The en-route navaids (VOR, DME,
NDB) designator is supposed to be unique (according to ICAO Annex 11)
within 600 NM. This means that these designators are not unique
world-wide. For airport navaids, there is no limitation.

FIXM adds two optional properties 'position' and 'navaidServiceType'
which may be used as a complement to the 'designator' information in
order to remove any ambiguity on the designator.

Important note: the combination of fields \[designator + position +
navaid service type\] shall not be interpreted as a natural key uniquely
identifying the navaid, in so far as producing and consuming
systems/services may use different aeronautical information sources with
different degree of precisions for lat/long, leading to small variations
of the position information. The supplementary fields shall be used for
disambiguation purposes only (i.e. plausibility checks based on position
and navaid service type) in case of duplicate/triplicate/…

OPTION 3 - Minimum reference with supplementary AIXM pointer

*(OPTION 3 = OPTION 1 + supplementary hypertext reference)*

Option 3 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

OPTION 4 - Complete reference

*(OPTION 4 = OPTION 2 + OPTION 3)*

Option 4 corresponds to the combination of Option 2 and Option 3. See
explanations above.

Examples (NOT for OPERATIONAL USE)

The table below depicts examples of FIXM references to fictitious VOR
DME “BOR” that is ‘published’ in AIXM 5.1 as part of the fictitious
[Donlon dataset](https://github.com/aixm/donlon/blob/master/Donlon.xml).
The data is entirely fictitious, located somewhere in the middle of the
Atlantic Ocean. The examples shall NEVER BE USED AS OPERATIONAL DATA.

<img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of Navaid references in FIXM</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>OPTION 1</strong></p>
<p>designator</p></td>
<td><p>&lt;fb:navaid&gt;</p>
<p>&lt;fb:designator&gt;BOR&lt;/fb:designator&gt;</p>
<p>&lt;/fb:navaid&gt;</p></td>
<td>This is the minimum reference that SHALL be provided.</td>
</tr>
<tr class="even">
<td><p><strong>OPTION 2</strong></p>
<p>designator<br />
+position<br />
+navaidServiceType</p></td>
<td><p>&lt;fb:navaid&gt;</p>
<p>&lt;fb:designator&gt;BOR&lt;/fb:designator&gt;</p>
<p>&lt;fb:navaidServiceType&gt;VOR_DME&lt;/fb:navaidServiceType&gt;</p>
<p>&lt;fb:position srsName="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;fb:pos&gt;52.36833333333333 -32.375&lt;/fb:pos&gt;</p>
<p>&lt;/fb:position&gt;</p>
<p>&lt;/fb:navaid&gt;</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>OPTION 3</strong></p>
<p>designator<br />
+href</p></td>
<td><p>&lt;fb:navaid href="urn:uuid:08a1bbd5-ea70-4fe3-836a-ea9686349495"&gt;</p>
<p>&lt;fb:designator&gt;BOR&lt;/fb:designator&gt;</p>
<p>&lt;/fb:navaid&gt;</p></td>
<td>Hypertext reference to be provided in accordance with the <a href="http://www.aixm.aero/sites/aixm.aero/files/imce/AIXM51/aixm_feature_identification_and_reference-1.0.pdf"><em>AIXM feature Identification and Reference document</em></a>, chapter 3.4.1.</td>
</tr>
<tr class="even">
<td><p><strong>OPTION 4</strong></p>
<p>designator<br />
+position<br />
+navaidServiceType<br />
+href</p></td>
<td><p>&lt;fb:navaid href="urn:uuid:08a1bbd5-ea70-4fe3-836a-ea9686349495"&gt;</p>
<p>&lt;fb:designator&gt;BOR&lt;/fb:designator&gt;</p>
<p>&lt;fb:navaidServiceType&gt;VOR_DME&lt;/fb:navaidServiceType&gt;</p>
<p>&lt;fb:position srsName="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;fb:pos&gt;52.36833333333333 -32.375&lt;/fb:pos&gt;</p>
<p>&lt;/fb:position&gt;</p>
<p>&lt;/fb:navaid&gt;</p></td>
<td></td>
</tr>
</tbody>
</table>

#### References to Aerodromes

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image15.png" style="width:2.75652in;height:2.14502in" /></p>
<p><em>UML Class <strong>AerodromeReference</strong> in package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:complexType name="AerodromeReferenceType"&gt;</p>
<p>&lt;xs:sequence&gt;</p>
<p>&lt;xs:element name="extension" type="fb:AerodromeReferenceExtensionType" nillable="true" minOccurs="0" maxOccurs="2000"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="iataDesignator" type="fb:IataAerodromeDesignatorType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="locationIndicator" type="fb:LocationIndicatorType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="name" type="fb:AerodromeNameType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="referencePoint" type="fb:GeographicalPositionType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;/xs:sequence&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Complex types <strong>AerodromeReferenceType</strong> in file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

The minimum aerodrome reference shall consist of the aerodrome location
indicator, if provided by ICAO Doc 7910 \[11\]. If the aerodrome has no
ICAO Doc 7910 location indicator, the minimum aerodrome reference shall
consist of the name of the aerodrome and its geographical location,
namely the aerodrome reference point.

OPTION 2 - Minimum reference with supplementary AIXM pointer

*(OPTION 2 = OPTION 1 + supplementary hypertext reference)*

Option 2 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

Examples (NOT for OPERATIONAL USE)

The table below depicts examples of FIXM references to fictitious
aerodrome “DONLON” that is ‘published’ in AIXM 5.1 as part of the
fictitious [Donlon
dataset](https://github.com/aixm/donlon/blob/master/Donlon.xml). The
data is entirely fictitious, located somewhere in the middle of the
Atlantic Ocean. The examples shall NEVER BE USED AS OPERATIONAL DATA.

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of aerodrome references in FIXM</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><strong>CASE 1 – The Aerodrome has an ICAO Doc 7910 location indicator</strong></td>
<td><strong>CASE 2 – The Aerodrome has no ICAO Doc. 7910 location indicator</strong></td>
</tr>
<tr class="even">
<td><p><strong>OPTION 1</strong></p>
<p>minimum</p></td>
<td><p>&lt;fx:destinationAerodrome&gt;</p>
<p>&lt;fb:locationIndicator&gt;EADD&lt;/fb:locationIndicator&gt;</p>
<p>&lt;/fx:destinationAerodrome&gt;</p></td>
<td><p>&lt;fx:destinationAerodrome&gt;</p>
<p>&lt;fb:name&gt;DONLON&lt;/fb:name&gt;</p>
<p>&lt;fb:referencePoint srsName="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;fb:pos&gt;52.3716666666667 -31.9494444444444&lt;/fb:pos&gt;</p>
<p>&lt;/fb:referencePoint&gt;</p>
<p>&lt;/fx:destinationAerodrome&gt;</p></td>
</tr>
<tr class="odd">
<td><p><strong>OPTION 2</strong></p>
<p>with href</p></td>
<td><p>&lt;fx:destinationAerodrome href="urn:uuid:1b54b2d6-a5ff-4e57-94c2-f4047a381c64"&gt;</p>
<p>&lt;fb:locationIndicator&gt;EADD&lt;/fb:locationIndicator&gt;</p>
<p>&lt;/fx:destinationAerodrome&gt;</p></td>
<td><p>&lt;fx:destinationAerodrome href="urn:uuid:1b54b2d6-a5ff-4e57-94c2-f4047a381c64"&gt;</p>
<p>&lt;fb:name&gt;DONLON&lt;/fb:name&gt;</p>
<p>&lt;fb:referencePoint srsName="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;fb:pos&gt;52.3716666666667 -31.9494444444444&lt;/fb:pos&gt;</p>
<p>&lt;/fb:referencePoint&gt;</p>
<p>&lt;/fx:destinationAerodrome&gt;</p></td>
</tr>
</tbody>
</table>

<img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />

Important note: FIXM enables the encoding of richer aerodrome
“reference” structures, such as

> &lt;fx:destinationAerodrome
> href="urn:uuid:1b54b2d6-a5ff-4e57-94c2-f4047a381c64"&gt;
>
> &lt;fb:iataDesignator&gt;DLN&lt;/fb:iataDesignator&gt;
>
> &lt;fb:locationIndicator&gt;EADD&lt;/fb:locationIndicator&gt;
>
> &lt;fb:name&gt;DONLON&lt;/fb:name&gt;
>
> &lt;fb:referencePoint srsName="urn:ogc:def:crs:EPSG::4326"&gt;
>
> &lt;fb:pos&gt;52.3716666666667 -31.9494444444444&lt;/fb:pos&gt;
>
> &lt;/fb:referencePoint&gt;
>
> &lt;/fx:destinationAerodrome&gt;

The provision of the name and reference point in addition to the
location indicator is technically possible but does not serve the
purpose of identifying the aerodrome. This implementation practice only
aims to provide consumers with richer information about the aerodrome
being referred to. Whether or not to use this supplementary information
is at the discretion of the consuming system / service.

#### References to Runway Directions

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image16.png" style="width:2.48696in;height:2.27903in" /></p>
<p><em>UML Class <strong>RunwayDirectionDesignator</strong> in package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:simpleType name="RestrictedRunwayDirectionDesignatorType"&gt;</p>
<p>&lt;xs:restriction base="fb:CharacterStringType"&gt;</p>
<p>&lt;xs:pattern value="(0[1-9]|[12][0-9]|3[0-6])[LRC]{0,1}"/&gt;</p>
<p>&lt;/xs:restriction&gt;</p>
<p>&lt;/xs:simpleType&gt;</p>
<p>&lt;xs:complexType name="RunwayDirectionDesignatorType"&gt;</p>
<p>&lt;xs:simpleContent&gt;</p>
<p>&lt;xs:extension base="fb:RestrictedRunwayDirectionDesignatorType"&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:extension&gt;</p>
<p>&lt;/xs:simpleContent&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Simple type <strong>RunwayDirectionDesignatorType</strong> in<br />
file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

The minimum Runway Direction reference shall consist of the Runway
Direction designator.

OPTION 2 - Minimum reference with supplementary AIXM pointer

*(OPTION 2 = OPTION 1 + supplementary hypertext reference)*

Option 2 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

Examples (NOT for OPERATIONAL USE)

The table below depicts examples of FIXM references to fictitious Runway
Direction “09L” that is ‘published’ in AIXM 5.1 as part of the
fictitious [Donlon
dataset](https://github.com/aixm/donlon/blob/master/Donlon.xml). The
data is entirely fictitious, located somewhere in the middle of the
Atlantic Ocean. The examples shall NEVER BE USED AS OPERATIONAL DATA.

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of Runway Direction references in FIXM</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>OPTION 1</strong></p>
<p>designator</p></td>
<td>&lt;fx:runwayDirection&gt;09L&lt;/fx:runwayDirection&gt;</td>
<td>This is the minimum reference that SHALL be provided.</td>
</tr>
<tr class="even">
<td><p><strong>OPTION 2</strong></p>
<p>designator<br />
+href</p></td>
<td>&lt;fx:runwayDirection href="urn:uuid:c8455a6b-9319-4bb7-b797-08e644342d64"&gt;09L&lt;/fx:runwayDirection&gt;</td>
<td>Hypertext reference to be provided in accordance with the <a href="http://www.aixm.aero/sites/aixm.aero/files/imce/AIXM51/aixm_feature_identification_and_reference-1.0.pdf"><em>AIXM feature Identification and Reference document</em></a>, chapter 3.4.1.</td>
</tr>
</tbody>
</table>

#### References to Enroute ATS routes

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image17.png" style="width:2.77633in;height:2.42466in" /></p>
<p><em>UML Class <strong>RouteDesignator</strong> in package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:simpleType name="RestrictedRouteDesignatorType"&gt;</p>
<p>&lt;xs:restriction base="fb:CharacterStringType"&gt;</p>
<p>&lt;xs:pattern value="[A-Z][A-Z0-9]{1,7}"/&gt;</p>
<p>&lt;/xs:restriction&gt;</p>
<p>&lt;/xs:simpleType&gt;</p>
<p>&lt;xs:complexType name="RouteDesignatorType"&gt;</p>
<p>&lt;xs:simpleContent&gt;</p>
<p>&lt;xs:extension base="fb:RestrictedRouteDesignatorType"&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:extension&gt;</p>
<p>&lt;/xs:simpleContent&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Simple type <strong>RouteDesignatorType</strong> in<br />
file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

The minimum Enroute ATS Route reference shall consist of the Enroute ATS
Route designator as published in the AIP. Enroute ATS Route designators
are not unique. However, the systematic pairing of an ATS route
designator with a route point (i.e. a significant point belonging to
that ATS route) in FIXM is considered sufficient for enabling
unambiguous identification of the ATS Route being referred to.

OPTION 2 - Minimum reference with supplementary AIXM pointer

*(OPTION 2 = OPTION 1 + supplementary hypertext reference)*

Option 2 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

Examples (NOT for OPERATIONAL USE)

The table below depicts examples of FIXM references to fictitious
Enroute ATS Route “UA4” that is ‘published’ in AIXM 5.1 as part of the
fictitious [Donlon
dataset](https://github.com/aixm/donlon/blob/master/Donlon.xml). The
data is entirely fictitious, located somewhere in the middle of the
Atlantic Ocean. The examples shall NEVER BE USED AS OPERATIONAL DATA.

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of EnRoute ATS Route references in FIXM</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>OPTION 1</strong></p>
<p>designator</p></td>
<td><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /> &lt;fx:routeDesignator&gt;UA4&lt;/fx:routeDesignator&gt;</td>
<td>This is the minimum reference that SHALL be provided.</td>
</tr>
<tr class="even">
<td><p><strong>OPTION 2</strong></p>
<p>designator<br />
+href</p></td>
<td><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />&lt;fx:routeDesignator href="urn:uuid:a14a8751-5428-46bc-a2d1-32ef84d37b5c"&gt;UA4&lt;/fx:routeDesignator&gt;</td>
<td>Hypertext reference to be provided in accordance with the <a href="http://www.aixm.aero/sites/aixm.aero/files/imce/AIXM51/aixm_feature_identification_and_reference-1.0.pdf"><em>AIXM feature Identification and Reference document</em></a>, chapter 3.4.1.</td>
</tr>
</tbody>
</table>

#### References to SIDs and STARs

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image18.png" style="width:2.71379in;height:1.875in" /></p>
<p><em>UML Classes <strong>SidStarReference</strong> package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:complexType name="SidStarReferenceType"&gt;</p>
<p>&lt;xs:sequence&gt;</p>
<p>&lt;xs:element name="abbreviatedDesignator" type="fb:SidStarAbbreviatedDesignatorType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="designator" type="fb:SidStarDesignatorType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="extension" type="fb:SidStarReferenceExtensionType" nillable="true" minOccurs="0" maxOccurs="2000"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;/xs:sequence&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p>&lt;xs:simpleType name="SidStarAbbreviatedDesignatorType"&gt;</p>
<p>&lt;xs:restriction base="fb:CharacterStringType"&gt;</p>
<p>&lt;xs:minLength value="1"/&gt;</p>
<p>&lt;xs:maxLength value="6"/&gt;</p>
<p>&lt;xs:pattern value="([A-Z]|[0-9])+([ \+\-/]*([A-Z]|[0-9])+)*"/&gt;</p>
<p>&lt;/xs:restriction&gt;</p>
<p>&lt;/xs:simpleType&gt;</p>
<p>&lt;xs:simpleType name="SidStarDesignatorType"&gt;</p>
<p>&lt;xs:restriction base="fb:CharacterStringType"&gt;</p>
<p>&lt;xs:minLength value="1"/&gt;</p>
<p>&lt;xs:maxLength value="7"/&gt;</p>
<p>&lt;xs:pattern value="([A-Z]|[0-9])+([ \+\-/]*([A-Z]|[0-9])+)*"/&gt;</p>
<p>&lt;/xs:restriction&gt;</p>
<p>&lt;/xs:simpleType&gt;</p>
<p><em>Simple types <strong>SidStarReferenceType</strong> in file<br />
AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

The minimum SID or STAR reference shall consist of the SID or STAR
designator as published in the AIP.

OPTION 2 - Minimum reference with supplementary AIXM pointer

*(OPTION 2 = OPTION 1 + supplementary hypertext reference)*

Option 2 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

Examples (NOT for OPERATIONAL USE)

The table below depicts examples of FIXM references to SID “AMOLO 5B”
that is published in the French AIPs.

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of SID references in FIXM</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>OPTION 1</strong></p>
<p>designator</p></td>
<td><p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /> &lt;fx:standardInstrumentDeparture&gt;</p>
<p>&lt;fb:designator&gt;AMOLO5B&lt;/fb:designator&gt;</p>
<p>&lt;/fx:standardInstrumentDeparture&gt;</p></td>
<td>This is the minimum reference that SHALL be provided.</td>
</tr>
<tr class="even">
<td><p><strong>OPTION 2</strong></p>
<p>designator<br />
+href</p></td>
<td><p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />&lt;fx:standardInstrumentDeparture href="urn:uuid:..."&gt;</p>
<p>&lt;fb:designator&gt;AMOLO5B&lt;/fb:designator&gt;</p>
<p>&lt;/fx:standardInstrumentDeparture&gt;</p></td>
<td>Hypertext reference to be provided in accordance with the <a href="http://www.aixm.aero/sites/aixm.aero/files/imce/AIXM51/aixm_feature_identification_and_reference-1.0.pdf"><em>AIXM feature Identification and Reference document</em></a>, chapter 3.4.1.</td>
</tr>
</tbody>
</table>

FIXM also supports the supplementary provision of the abbreviated
designator of the SID or the STAR which is commonly used in FMS
databases and in some ground automation systems. The ‘abbreviated
designator’, if provided, should be the designator obtained after
applying the rules for shortening names specified by the ARINC 424
specification, chapter 7.4. Example:

> &lt;fx:standardInstrumentDeparture&gt;
>
> &lt;fb:abbreviatedDesignator&gt;AMOL5B&lt;/fb:abbreviatedDesignator&gt;
>
> &lt;fb:designator&gt;AMOLO5B&lt;/fb:designator&gt;
>
> &lt;/fx:standardInstrumentDeparture&gt;

#### References to Airspace

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image19.png" style="width:2.4375in;height:1.88479in" /></p>
<p><em>UML Class <strong>AirspaceDesignator</strong> in package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:simpleType name="RestrictedAirspaceDesignatorType"&gt;</p>
<p>&lt;xs:restriction base="fb:CharacterStringType"&gt;</p>
<p>&lt;xs:minLength value="1"/&gt;</p>
<p>&lt;xs:maxLength value="10"/&gt;</p>
<p>&lt;xs:pattern value="([A-Z]|[0-9]|[, !&amp;quot;&amp;amp;#$%'\(\)\*\+\-\./:;&amp;lt;=&amp;gt;\?@\[\\\]\^_\|\{\}])*"/&gt;</p>
<p>&lt;/xs:restriction&gt;</p>
<p>&lt;/xs:simpleType&gt;</p>
<p>&lt;xs:complexType name="AirspaceDesignatorType"&gt;</p>
<p>&lt;xs:simpleContent&gt;</p>
<p>&lt;xs:extension base="fb:RestrictedAirspaceDesignatorType"&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:extension&gt;</p>
<p>&lt;/xs:simpleContent&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Simple type <strong>AirspaceDesignatorType</strong> in<br />
file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

The minimum airspace reference shall consist of the airspace location
indicator, if provided by ICAO Doc 7910 \[11\]. If the airspace has no
ICAO Doc 7910 location indicator, the minimum airspace reference shall
consist of the coded designator of the airspace as published in the AIP.

OPTION 2 - Minimum reference with supplementary AIXM pointer

*(OPTION 2 = OPTION 1 + supplementary hypertext reference)*

Option 2 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

Examples (NOT for OPERATIONAL USE)

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of Airspace references in FIXM</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><strong>CASE 1 – The Airspace has an ICAO Doc 7910 location indicator</strong></td>
<td><strong>CASE 2 – The Airspace has no ICAO Doc. 7910 location indicator</strong></td>
</tr>
<tr class="even">
<td><p><strong>OPTION 1</strong></p>
<p>designator</p></td>
<td><p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /></p>
<p>&lt;fx:region&gt;KZLC&lt;/fx:region&gt;</p></td>
<td><p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /></p>
<p>&lt;fx:region&gt;AMSWELL&lt;/fx:region&gt;</p></td>
</tr>
<tr class="odd">
<td><p><strong>OPTION 2</strong></p>
<p>designator<br />
+href</p></td>
<td><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />&lt;fx:region href="urn:uuid:..."&gt;KZLC&lt;/fx:region&gt;</td>
<td><p>&lt;fx:region href="urn:uuid:..."&gt;AMSWELL&lt;/fx:region&gt;</p>
<p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /></p>
<p><em>(from DONLON dataset)</em></p></td>
</tr>
</tbody>
</table>

#### References to (ATC) Units

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image20.png" style="width:2.97919in;height:2.14151in" /></p>
<p><em>UML Class <strong>ATCUnitReference</strong> in package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:complexType name="AtcUnitReferenceType"&gt;</p>
<p>&lt;xs:sequence&gt;</p>
<p>&lt;xs:element name="atcUnitNameOrAlternate" type="fb:TextNameType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="controlSectorDesignator" type="fb:AirspaceDesignatorType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="extension" type="fb:AtcUnitReferenceExtensionType" nillable="true" minOccurs="0" maxOccurs="2000"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="locationIndicator" type="fb:LocationIndicatorType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="position" type="fb:GeographicalPositionType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;/xs:sequence&gt;</p>
<p>&lt;xs:attribute name="href" type="fb:HypertextReferenceType" use="optional"&gt;</p>
<p>&lt;/xs:attribute&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Complex type <strong>ATCUnitReferenceType</strong> in file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

OPTION 1 - Minimum reference

The minimum ATC unit reference shall consist of the location indicator
of the unit, if provided by ICAO Doc 7910 \[11\]. If the unit has no
ICAO Doc 7910 location indicator, the minimum airspace reference shall
consist of the name of the unit or any alternate name, as published in
the AIP.

OPTION 2 - Minimum reference with supplementary AIXM pointer

*(OPTION 2 = OPTION 1 + supplementary hypertext reference)*

Option 2 corresponds to Option 1 with an additional hypertext reference
as described in chapter Generic hypertext references.

Examples (NOT for OPERATIONAL USE)

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of Unit references in FIXM</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><strong>CASE 1 – The Unit has an ICAO Doc 7910 location indicator</strong></td>
<td><strong>CASE 2 – The Unit has no ICAO Doc. 7910 location indicator</strong></td>
</tr>
<tr class="even">
<td><p><strong>OPTION 1</strong></p>
<p>designator</p></td>
<td><p>&lt;fx:originator&gt;</p>
<p>&lt;fb:locationIndicator&gt;EBBU&lt;/fb:locationIndicator&gt;</p>
<p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />&lt;/fx:originator&gt;</p></td>
<td><p>&lt;fx:originator&gt;</p>
<p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /> &lt;fb:atcUnitNameOrAlternate&gt;MILITARY DONLON TWR&lt;/fb:atcUnitNameOrAlternate&gt;</p>
<p>&lt;/fx:originator&gt;</p></td>
</tr>
<tr class="odd">
<td><p><strong>OPTION 2</strong></p>
<p>designator<br />
+href</p></td>
<td><p>&lt;fx:originator href="urn:uuid:..."&gt;</p>
<p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /> &lt;fb:locationIndicator&gt;EBBU&lt;/fb:locationIndicator&gt;</p>
<p>&lt;/fx:originator&gt;</p></td>
<td><p>&lt;fx:originator href="urn:uuid:..."&gt;</p>
<p><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /> &lt;fb:atcUnitNameOrAlternate&gt;MILITARY DONLON TWR&lt;/fb:atcUnitNameOrAlternate&gt;</p>
<p>&lt;/fx:originator&gt;</p></td>
</tr>
</tbody>
</table>

### Relative points

<table>
<thead>
<tr class="header">
<th><strong>FIXM Logical Model</strong></th>
<th><strong>FIXM XML schemas</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image21.png" style="width:2.73585in;height:3.49573in" /></p>
<p><em>UML Class <strong>RelativePoint</strong> in package FIXM.Base.AeronauticalReference</em></p></td>
<td><p>&lt;xs:complexType name="RelativePointType"&gt;</p>
<p>&lt;xs:sequence&gt;</p>
<p>&lt;xs:element name="bearing" type="fb:BearingType" minOccurs="1" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="distance" type="fb:DistanceType" minOccurs="1" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="extension" type="fb:RelativePointExtensionType" nillable="true" minOccurs="0" maxOccurs="2000"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="position" type="fb:GeographicalPositionType" nillable="true" minOccurs="0" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;xs:element name="referencePoint" type="fb:NavaidType" minOccurs="1" maxOccurs="1"&gt;</p>
<p>&lt;/xs:element&gt;</p>
<p>&lt;/xs:sequence&gt;</p>
<p>&lt;/xs:complexType&gt;</p>
<p><em>Complex type <strong>RelativePointType</strong> in<br />
file AeronauticalReference.xsd</em></p></td>
</tr>
</tbody>
</table>

A relative point is a bearing and distance from a reference navaid.
Encoding a relative point in FIXM requires the ‘bearing’, ‘distance’ and
‘referencePoint’ properties to be provided. All of these properties
shall be provided.

FIXM enables a relative point to be supplemented with an optional
‘position’ value for storing the actual position of the relative point
if already known. The exchange of this information may prove useful in
order to save consuming systems / services from (re)computing the
position of the relative point. Whether or not to use this supplementary
information is at the discretion of the consuming system / service.

Examples (NOT for OPERATIONAL USE)

The table below depicts examples of FIXM encodings of relative points
that are derived from the fictitious [Donlon
dataset](https://github.com/aixm/donlon/blob/master/Donlon.xml). The
data is entirely fictitious, located somewhere in the middle of the
Atlantic Ocean. The examples shall NEVER BE USED AS OPERATIONAL DATA.

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Examples of relative point in FIXM</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><strong>Without position information</strong></td>
<td><p>&lt;fb:relativePoint&gt;</p>
<p>&lt;fb:bearing uom="DEG" zeroBearingType="MAGNETIC_NORTH"&gt;82.0&lt;/fb:bearing&gt;</p>
<p>&lt;fb:distance uom="NM"&gt;2.0&lt;/fb:distance&gt;</p>
<p>&lt;fb:referencePoint&gt;</p>
<p>&lt;fb:designator&gt;BOR&lt;/fb:designator&gt; (*)</p>
<p>&lt;/fb:referencePoint&gt;</p>
<p>&lt;/fb:relativePoint&gt;</p></td>
<td>(*) See chapter References to Navaid above. All four options can be used for encoding this reference. OPTION 1 is used in this example.</td>
</tr>
<tr class="even">
<td><img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><strong>With position information</strong></td>
<td><p>&lt;fb:relativePoint&gt;</p>
<p>&lt;fb:bearing uom="DEG" zeroBearingType="TRUE_NORTH"&gt;180&lt;/fb:bearing&gt;</p>
<p>&lt;fb:distance uom="NM"&gt;60.0&lt;/fb:distance&gt;</p>
<p>&lt;fb:position srsName="urn:ogc:def:crs:EPSG::4326"&gt;</p>
<p>&lt;fb:pos&gt;51.36833333333333 -32.375&lt;/fb:pos&gt;</p>
<p>&lt;/fb:position&gt;</p>
<p>&lt;fb:referencePoint&gt;</p>
<p>&lt;fb:designator&gt;BOR&lt;/fb:designator&gt; (*)</p>
<p>&lt;/fb:referencePoint&gt;</p>
<p>&lt;/fb:relativePoint&gt;</p></td>
<td></td>
</tr>
</tbody>
</table>

### Vertical distances

**Definitions**

The term vertical distance collectively refers to altitudes, elevations
and heights, as defined by
ICAO<img src=".//media/image22.emf" style="width:6.26806in;height:2.97774in" />

<span id="_Toc48643983" class="anchor"></span>Figure 6: Differences
between Elevation, Altitude, Height and Ellipsoid height

-   **Altitude** = The vertical distance of a level, a point or an
    object considered as a point, measured from mean sea level (MSL).
    **\[ICAO\]**

-   **Elevation** = The vertical distance of a point or a level, on or
    affixed to the surface of the earth, measured from mean sea level.
    **\[ICAO\]**

-   **Height** = The vertical distance of a level, a point or an object
    considered as a point, measured from a specified datum. **\[ICAO\]**

-   **Ellipsoid height** = The height related to the reference
    ellipsoid, measured along the ellipsoidal outer normal through the
    point in question. **\[ICAO\]**

**FIXM representation of vertical distances**

FIXM supports the representation of altitudes expressed in feet or
meters (FIXM construct ‘Altitude’), of altitudes expressed as flight
level number or standard metric level (FIXM construct ‘FlightLevel’) and
of ellipsoid heights & heights SFC expressed in feet or meter (FIXM
construct ‘Height’ used in conjunction with a VerticalReference).

<img src=".//media/image23.png" style="width:5.97761in;height:4.0142in" />

These vertical distances are specialisations of the generic class
Measure which serves as the parent class for all measure types including
speeds, angles, pressures, temperatures etc. Therefore, altitudes,
flight levels and heights are always encoded as double values, although
integer values are expected. “Double Integer” conversion can be handled
differently depending on the technical context. This may lead to e.g.
flight level value 100 being expressed as 100.00…0001 and the flight
level value 101 being expressed as 100.99…99999. It is acknowledged that
the current FIXM design may create value persistence problem across
applications, in particular if rounding or truncation are applied
further down. FIXM implementers are therefore invited to verify the
persistence of vertical distances values across their software.

**Examples**

The following examples show valid FIXM encoding of altitudes and flight
levels expressed as integer.

> &lt;fb:altitude uom="FT"&gt;10000&lt;/fb:altitude&gt;
>
> &lt;fb:altitude uom="M"&gt;3500&lt;/fb:altitude&gt;
>
> &lt;fb:flightLevel uom="FL"&gt;290&lt;/fb:flightLevel&gt;
>
> &lt;fb:flightLevel uom="SM"&gt;1130&lt;/fb:flightLevel&gt;

The following example shows the encoding of a flight level expressed as
a double. This encoding is technically permitted by FIXM but is NOT
recommended.

> &lt;fb:flightLevel uom="FL"&gt;290.0&lt;/fb:flightLevel&gt;

### Sequence numbers

The FIXM Logical Model specifies several ordered repeating sequences.
The FIXM XML schemas add an optional sequence number attribute to the
repeating elements in order to ensure that the order of a sequence is
always preserved, even after XSLT manipulation.

The sequence number should be a sequentially increasing integer with a
value beginning at zero. These sequence numbers are only meant for
ordering, not identification, purposes. As such, the set of sequence
numbers taken as a whole should always be contiguous. If an element were
removed from a sequence, the numbering in subsequent representations
should be reset to reflect this, not maintained so that a gap is formed.

Example

<img src=".//media/image2.png" style="width:0.42708in;height:0.42708in" />

### Contact Information

<img src=".//media/image24.png" style="width:4.4438in;height:4.42945in" />

<u>Postal Address</u>

TODO

<u>Telephone Contact</u>

TODO

<u>Online Contact</u>

In FIXM, the online contact information can include an email address
and/or a network address.

A network address is always formed of two pieces of information: the
**linkage** and the **network** information.

-   The former captures the expression of the network address. This is
    supported by property OnlineContact.linkage.

-   The latter captures the network on which the address is valid. This
    is supported by property OnlineContact.network.

Property OnlineContact.network provides a choice between predefined
network types and free text. Network information should be preferably
encoded using the property NetworkChoice.**type** populated with the
applicable enumerated value from enumeration TelecomNetworkType. If none
of the enumerated values is suitable, the property NetworkChoice.other
shall be used. The ATM Information Reference Model provides additional
telecom network types that should be used for populating
NetworkChoice.other, as appropriate. These additional AIRM values are
available at the following link:

<http://airm.aero/viewer/1.0.0/logical-model.html#CodeTelecomNetworkType>

The type of network affects the format of the linkage information.

-   When the network is INTERNET, the linkage should be a resolvable URL

-   When the network is AFTN, the linkage should be a valid AFTN address

Examples

The following example illustrates contact information formed of an email
address and an Internet address expressed as a resolvable URL.

> &lt;fb:onlineContact&gt;
>
> &lt;fb:email&gt;fixm.secretariat@eurocontrol.int&lt;/fb:email&gt;
>
> &lt;fb:linkage&gt;https://www.fixm.aero/content/contact.pl&lt;/fb:linkage&gt;
>
> &lt;fb:network&gt;
>
> &lt;fb:type&gt;INTERNET&lt;/fb:type&gt;
>
> &lt;/fb:network&gt;
>
> &lt;/fb:onlineContact&gt;

The following example illustrates contact information formed of an AFTN
address. The example features the EUROCONTROL NM ‘AFTN address’ for
Flight Plan Message Submission to IFPS (FP1 - Brussels (Haren)).

> &lt;fb:onlineContact&gt;
>
> &lt;fb:linkage&gt;EUCHZMFP&lt;/fb:linkage&gt;
>
> &lt;fb:network&gt;
>
> &lt;fb:type&gt;AFTN&lt;/fb:type&gt;
>
> &lt;/fb:network&gt;
>
> &lt;/fb:onlineContact&gt;

The following example illustrates contact information formed of a SITA
address. ‘SITA’ is not a value captured in FIXM enumeration
TelecomNetworkType but is part of the reference ATM vocabulary provided
by the AIRM ([AIRM codelist
CodeTelecomNetworkType](http://airm.aero/viewer/1.0.0/logical-model.html#CodeTelecomNetworkType)).
The example features the EUROCONTROL NM ‘SITA address’ for Flight Plan
Message Submission to IFPS (FP1 - Brussels (Haren)).

> &lt;fb:onlineContact&gt;
>
> &lt;fb:linkage&gt;BRUEP7X&lt;/fb:linkage&gt;
>
> &lt;fb:network&gt;
>
> &lt;fb:other&gt;SITA&lt;/fb:other&gt;
>
> &lt;/fb:network&gt;
>
> &lt;/fb:onlineContact&gt;

### Version numbers

*This is a placeholder for further guidance on how to encode version
numbers. This chapter will be populated in a future version of the
document.*

### Aircraft Types

*This is a placeholder for further guidance on how to encode aircraft
types. This chapter will be populated in a future version of the
document.*

### Rules for encoding a 4D Trajectory 

*This is a placeholder for further guidance on how to encode a 4D
trajectory. This chapter will be populated in a future version of the
document.*

### Rules for encoding Constraints 

*This is a placeholder for further guidance on how to encode
constraints. This chapter will be populated in a future version of the
document.*

### General rules for data correctness

*Important note: in the present version of the document, limited effort
could be spent on the documentation of FIXM business rules addressing
data correctness. The list below provides an initial set of rules that
were identified during the writing of this document or that are already
captured in the FIXM model as model element notes. Future versions of
the document will enrich this table based on implementers’ feedback, and
may also revisit the overall formulation and description method for
these rules, in particular in the light of the [AIXM experience with
regards to business rules](http://aixm.aero/page/business-rules).*

<table>
<thead>
<tr class="header">
<th><strong>FIXM model element</strong></th>
<th><strong>Business rule description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GeograhicalPosition</td>
<td>When encoding geographical positions, special values INF, -INF and NaN are not allowed.</td>
</tr>
<tr class="even">
<td><p>ContactInformation,</p>
<p>PersonOrOrganization</p></td>
<td>If the usage of ContactInformation is associated with a person, the ContactInformation.name field should not be used and the PersonOrOrganization.name should be used instead.</td>
</tr>
<tr class="odd">
<td>PostalAddress</td>
<td>The countryName shall always be populated with the full name, not an ISO 3166 abbreviation.</td>
</tr>
<tr class="even">
<td>PostalAddress</td>
<td>CountryCode shall always be populated using an ISO 3166 abbreviation.</td>
</tr>
<tr class="odd">
<td>OnlineContact</td>
<td>If OnlineContact.network.type=INTERNET, the OnlineContact.linkage shall be expressed as a valid URL.</td>
</tr>
<tr class="even">
<td>OnlineContact</td>
<td>If OnlineContact.network.type=AFTN, the OnlineContact.linkage shall be expressed as a valid AFTN address.</td>
</tr>
<tr class="odd">
<td>AerodromeReference</td>
<td>The locationIndicator shall be a valid code provided by ICAO Doc 7910.</td>
</tr>
<tr class="even">
<td>VerticalRange</td>
<td>The lowerBound shall always be lower than the upperBound.</td>
</tr>
<tr class="odd">
<td>TrueAirspeedRange</td>
<td>The lowerSpeed shall always be lower than the upperSpeed.</td>
</tr>
<tr class="even">
<td>TimeRange</td>
<td>The earliest time shall always be before the latest time.</td>
</tr>
<tr class="odd">
<td>Aircraft</td>
<td>The property formationCount, if provided, shall be equal to or greater than 2.</td>
</tr>
<tr class="even">
<td>Aircraft, AircraftType</td>
<td>The sum of all the AircraftType.numberOfAircraft properties, if provided, shall match Aircraft.formationCount.</td>
</tr>
<tr class="odd">
<td>OnlineContact</td>
<td>The OnlineContact.network shall be always populated when providing an OnlineContact.linkage.</td>
</tr>
</tbody>
</table>

### Rules for absent data

FIXM supports the representation of fields that are explicitly absent or
that are deleted. It does so by leveraging the XSD specification for
Elements which includes the *nillable* attribute. This “nillable”
attribute specifies whether an explicit null value can be assigned to
the element. When nillable is set to “true” in the element definition,
this in turn enables an instance of the element to have the built-in nil
attribute with a value set to “true”. Example:

> &lt;xs:complexType name="FlightType"&gt;  
> \[...\]  
> &lt;xs:element name="dangerousGoods" type="fx:DangerousGoodsType"
> **nillable="true"** \[...\]&gt;  
> \[...\]  
> &lt;/xs:complexType&gt;
>
> &lt;fx:Flight&gt;  
> &lt;fx:dangerousGoods **xsi:nil="true"**/&gt;  
> &lt;/fx:Flight&gt;

FIXM does not support the exchange of a “nil reason” to explain why an
element is nil. The interpretation of a nil element therefore depends on
the context of the information exchange:

-   A nil element included in an FF-ICE Flight Plan Update message will
    indicate that this flight plan data item is to be deleted. This
    interpretation is dictated by the FF-ICE Implementation Guidance
    Manual which states the following:

> *7.4.3.6 A Flight Plan Update is only required to contain those items
> that have changed (in addition to the mandatory items specified for an
> Update message), i.e. it is not necessary to resend complete flight
> data. Data items that were included in the previous version of the
> flight plan and have not been included in the Flight Plan Update will
> remain unchanged. This means that a mechanism is required to identify
> when a flight plan data item is to be deleted.”*

-   A nil element included in an FF-ICE Flight Data Response Message
    will indicate that the data item is explicitly declared as not
    available to the flight data requestor.

Future FIXM versions may support the exchange of an additional “nil
reason” attribute, if the need for it is identified by the FIXM
Community.

*Note: the support for nillable elements has implied a significant
design change in FIXM Core 4.2.0. The previous FIXM Core versions relied
extensively on XSD attributes, which are not nillable. These XSD
attributes were converted to XSD elements in FIXM Core 4.2.0 so that the
built-in XSD attribute nillable could be leveraged.*

##### Declaring null Measures and Geographical Position

The FIXM Measures types enforce the provision of the “uom” attribute
together with the numeric value of the measure. Likewise, the FIXM
Geographical Position type enforces the provision of the srsName
attribute “urn:ogc:def:crs:EPSG::4326” together with the position. This
design guarantees that the required unit of measure and coordinate
reference system are always provided in order to enable the correct
interpretation of measures and positions. However, it requires a special
workaround when null values are to be exchanged.

The provision of a null value for a measure or a position still requires
the mandatory attribute “uom” or “srsName” to be provided, even if
meaningless. For instance, the following XML data would NOT validate
against the FIXM Core schema, because the uom for a Mass is missing.

<img src=".//media/image25.png" style="width:0.23403in;height:0.23403in" />&lt;fx:desired&gt;

&lt;fx:takeoffMass xsi:nil="true/"&gt;

&lt;/fx:desired&gt;

Therefore, the following rules apply when declaring null Measures or
Geographical Position.

When a measure is to be declared null,

-   Information provider side: Provide a fake uom in order to ensure
    proper schema validation

-   Information consumer side: Ignore the fake uom provided together
    with the null measure

When a geographical position is to be declared null:

-   Information provider side: Provide the srsName
    “urn:ogc:def:crs:EPSG::4326” in order to ensure proper schema
    validation

-   Information consumer side: Ignore the provided srsName provided
    together with the null position.

Example of valid null measure declaration with a fake uom to be ignored:

> <img src=".//media/image26.png" style="width:0.26389in;height:0.26389in" />&lt;fx:desired&gt;
>
> &lt;fx:takeoffMass xsi:nil="true" uom="KG"/&gt;
>
> &lt;/fx:desired&gt;

