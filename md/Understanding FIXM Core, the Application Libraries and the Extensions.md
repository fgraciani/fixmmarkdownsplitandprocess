## Understanding FIXM Core, the Application Libraries and the Extensions

### FIXM Core

#### What is it?

**FIXM Core** provides globally harmonized flight data structures that
can be exchanged in various contexts. The main context for the use of
**FIXM Core** is ICAO FF-ICE. Therefore, **FIXM Core** currently
captures the flight data structures that are identified in the ICAO
FF-ICE Implementation Guidance Manual 0.91. Only flight data structures
that are globally applicable qualify for FIXM Core. Flight data
structures that are local or regional in nature do not qualify for
**FIXM Core**. An **Extensions** mechanism is implemented so that **FIXM
Core** can be extended in order to cover these local or regional data
structures, as appropriate.

**FIXM Core** exists as a standard for exchanging flight data rather
than as a set of pre-defined messages, allowing flexible exchanges
between users rather than enforcing rigid communication patterns.
However, once a given exchange is well-defined, it is useful to be able
to enforce syntax and content validation checks to ensure the data being
exchanged is of high quality. This is addressed by **Application
Libraries**.

#### What is a valid FIXM Core usage?

The general requirements for a valid **FIXM Core** usage are the
following:

| **REQUIREMENT ON DATA STRUCTURE** |                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Requirement**                   | To qualify as valid usage of FIXM Core, the flight-related content of a given message, or relevant part thereof, shall be syntactically valid against the FIXM Core XML Schemas.                                                                                                                                                |
| **Rationale**                     | The valid usage of FIXM Core implies that the flight-related content of a message exchanged between two parties is valid against the FIXM Core XML Schemas. If a message includes additional information not in scope of FIXM Core, it must be structured so that its relevant part is valid against the FIXM Core XML Schemas. |
| **Important note**                | Being syntactically valid against the FIXM Core XML Schemas implies the FIXM Core hierarchy is respected. FIXM Core is not expected to be used only as a library of flight datatypes.                                                                                                                                           |
| **How to check this**             | The content of a message, or relevant part thereof, validates without error against the FIXM Core XML schemas when tested / parsed by XML validation tools.                                                                                                                                                                     |

Example of FIXM core usage satisfying the requirement on data structure

> <img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />&lt;fx:aerodrome&gt;
>
> &lt;fb:locationIndicator&gt;EBBR&lt;/fb:locationIndicator&gt;
>
> &lt;/fx:aerodrome&gt;

This example displays an aerodrome reference involving a four-letter
ICAO location indicator. It complies with the structural rules for
aerodrome references defined by the FIXM Core XML schemas.

Examples of FIXM core usage **NOT** satisfying the requirement on data
structure

> <img src=".//media/image3.png" style="width:0.25in;height:0.25in" />&lt;fx:aerodrome&gt;
>
> &lt;fb:locationIndicator&gt;BRU&lt;/fb:locationIndicator&gt;
>
> &lt;/fx:aerodrome&gt;

This example displays an aerodrome reference based on property
locationIndicator. The value “BRU” does not respect the pattern
\[A-Z\]{4} enforced by FIXM for property locationIndicator. This example
does NOT comply with the structural rules for aerodrome references
defined by the FIXM XML schemas and does not qualify as valid FIXM
usage.

-----

This example below features a valid XML schema that defines a Flight
Identification structure comprising the departure & arrival aerodrome
references, the aircraft identification and the estimated off-block
time. It also features an example XML sample that is valid against this
schema.

> <img src=".//media/image3.png" style="width:0.25in;height:0.25in" />&lt;xs:schema
> xmlns:wrong="fixm\_as\_library\_of\_types"
> xmlns:fx="http://www.fixm.aero/flight/4.2"
> xmlns:fb="http://www.fixm.aero/base/4.2"\[…\] &gt;  
> \[...\]  
> &lt;xs:element name="FlightIdentification"
> type="wrong:FlightIdentificationType"/&gt;  
> &lt;xs:complexType name="FlightIdentificationType"&gt;  
> &lt;xs:sequence&gt;  
> &lt;xs:element name="departureAerodrome"
> type="fb:AerodromeReferenceType"/&gt;  
> &lt;xs:element name="arrivalAerodrome"
> type="fb:AerodromeReferenceType"/&gt;  
> &lt;xs:element name="ACID" type="fb:AircraftIdentificationType"/&gt;  
> &lt;xs:element name="EOBT" type="fb:TimeType"/&gt;  
> &lt;/xs:sequence&gt;  
> &lt;/xs:complexType&gt;  
> &lt;/xs:schema&gt;
>
> <img src=".//media/image3.png" style="width:0.25in;height:0.25in" />&lt;wrong:FlightIdentification
> xmlns:wrong=\[…\] xmlns:fb="http://www.fixm.aero/base/4.2"
> xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
> xs:schemaLocation=\[…\]"&gt;
>
> &lt;wrong:departureAerodrome&gt;
>
> &lt;fb:name&gt;LES BARAQUES&lt;/fb:name&gt;
>
> &lt;/wrong:departureAerodrome&gt;
>
> &lt;wrong:arrivalAerodrome&gt;
>
> &lt;fb:name&gt;NORTHFALL MEADOW&lt;/fb:name&gt;
>
> &lt;/wrong:arrivalAerodrome&gt;
>
> &lt;wrong:ACID&gt;BLXI&lt;/wrong:ACID&gt;
>
> &lt;wrong:EOBT&gt;1909-07-25T04:41:00.000Z&lt;/wrong:EOBT&gt;
>
> &lt;/wrong:FlightIdentification&gt;
>
> &lt;!--
> https://en.wikipedia.org/wiki/Louis\_Bl%C3%A9riot\#1909\_Channel\_crossing
> --&gt;

The example schema above is not FIXM Core and is not a FIXM extension.
It is a fictitious, standalone XML schema that defines its own hierarchy
of elements, but which reuses types from the core FIXM XML schemas for
typing these elements. The reuse of FIXM datatypes is highlighted in
blue in the schema description.

This example illustrates the reuse of FIXM Core as a library of
datatypes. While this practice is technically feasible and produces
valid schemas, it is not considered a valid FIXM Core usage because it
breaks the hierarchy of properties defined by FIXM Core. An information
service relying on such an implementation practice would fail to satisfy
the FIXM Core requirement on data structure.

-----

| **REQUIREMENT ON DATA CORRECTNESS** |                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Requirement**                     | To qualify as valid usage of FIXM core, the flight-related content of a given message, or relevant part thereof, shall satisfy the minimum set of rules addressing data plausibility and consistency.                                                                                                                                                                                            |
| **Rationale**                       | The flight-related content of a message being syntactically correct and complete may still not make sense from an operational or plausibility perspective. Additional business rules are required to check the correctness of the encoded information, such as the consistency between model elements.                                                                                           |
| **How to check this**               | The content of a message, or the relevant part thereof, validates without error against the applicable business rules addressing data correctness. Chapter 2.4.13 lists business rules addressing data correctness which are always applicable whatever the context of the exchange. Additional business rules addressing data correctness may exist which are specific to particular use-cases. |

<img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" />Example
of FIXM core usage satisfying the requirement on data correctness

> &lt;fx:verticalRange&gt;
>
> &lt;fb:lowerBound&gt;
>
> &lt;fb:flightLevel uom="FL"&gt;240&lt;/fb:flightLevel&gt;
>
> &lt;/fb:lowerBound&gt;
>
> &lt;fb:upperBound&gt;
>
> &lt;fb:flightLevel uom="FL"&gt;250&lt;/fb:flightLevel&gt;
>
> &lt;/fb:upperBound&gt;
>
> &lt;/fx:verticalRange&gt;

This example shows the FIXM encoding of vertical range \[FL240;FL250\].
It satisfies the basic data plausibility/correctness rule “*The
lowerBound shall always be lower than the upperBound*” that is
identified in Chapter 2.4.13. It qualifies as valid FIXM core usage.

Example of FIXM core usage NOT satisfying the requirement on data
correctness

> <img src=".//media/image3.png" style="width:0.25in;height:0.25in" />&lt;fx:aircraft&gt;
>
> &lt;fx:aircraftType&gt;
>
> &lt;fx:numberOfAircraft&gt;2&lt;/fx:numberOfAircraft&gt;
>
> &lt;fx:type&gt;
>
> &lt;fx:icaoAircraftTypeDesignator&gt;MIR2&lt;/fx:icaoAircraftTypeDesignator&gt;
>
> &lt;/fx:type&gt;
>
> &lt;/fx:aircraftType&gt;
>
> &lt;fx:aircraftType&gt;
>
> &lt;fx:numberOfAircraft&gt;1&lt;/fx:numberOfAircraft&gt;
>
> &lt;fx:type&gt;
>
> &lt;fx:icaoAircraftTypeDesignator&gt;RFAL&lt;/fx:icaoAircraftTypeDesignator&gt;
>
> &lt;/fx:type&gt;
>
> &lt;/fx:aircraftType&gt;
>
> &lt;fx:formationCount&gt;2&lt;/fx:formationCount&gt;
>
> &lt;/fx:aircraft&gt;

This example represents a description of a fictitious formation of
military aircraft composed of two Mirages 2000 and one Rafale which
altogether constitute a single (formation) flight. This example is valid
from a data structure point of view (it validates against the FIXM core
XML schemas) but is not correct in so far as the sum of all
AircraftType.numberOfAircraft properties does not match
Aircraft.formationCount, which breaks a rule from Chapter 2.4.13. This
example does not qualify as valid FIXM core usage.

### Application Libraries

#### What is it?

An **Application Library** is a FIXM component that addresses the use of
FIXM Core in a given context. It can be of global, regional or local
applicability, depending on the context. An **Application Library**
essentially provides context-specific **‘message data structures’** and
**‘message templates’** which enables harmonized representation of the
FIXM-based messages exchanged using SWIM information services, as
outlined in the figure below.

<img src=".//media/image4.png" style="width:2.81504in;height:3.56522in" />

<span id="_Toc48643978" class="anchor"></span>Figure 1: General
structure of a message and role of an Application Library

<img src=".//media/image5.png" style="width:1.66806in;height:2.1125in" />An
**Application Library** captures messaging related data elements and
reuses and restricts relevant subsets of the FIXM Core data structures.
FIXM Core is independent and does not require an update when changes in
an application library occur.

An **Application Library** may also leverage **Extensions**, as
illustrated on the picture opposite.

An example of an Application Library is the **FF-ICE Application
Library** developed and released by the FIXM CCB. This library addresses
the use of FIXM core in the specific context of FF-ICE. It provides
harmonized FF-ICE Message data structure (e.g. data structures for
representing the FF-ICE Filing Status, the FF-ICE Planning Status etc.)
and the FF-ICE message templates (e.g. the template for the FF-ICE Filed
Flight Plan Message, the template for the FF-ICE Flight Cancellation
Message etc.), in line with the FF-ICE Implementation Guidance Manual.

More details about this FF-ICE Application Library can be found in
Chapter 3.2 .

#### Message Data Structures

Message Data structures designate at high level the data structures that
are necessary for understanding the meaning and purpose of the
information that is exchanged in a given context. They commonly include
message identifiers and timestamps, codes identifying business types of
messages, and any context-specific data that qualify the associated
message interactions[2].

Examples of message data structures can be found in the FF-ICE
Implementation Guidance Manual. The Figure below shows the message data
structures associated with the FF-ICE Flight Cancellation Message.

<img src=".//media/image6.png" style="width:2.36522in;height:3.62891in" />

<span id="_Toc48643979" class="anchor"></span>Figure 2: Example of
Message Data structures from FF-ICE

#### Message Templates

A message template is a more restrictive subset of message and flight
data structures that is relevant to a given information exchange. In
SWIM terms, a message template provides guidance for formatting a given
information service payload.

By removing unused fields, adjusting multiplicities, and adding or
further limiting pattern constraints, a template can tailor the broad
standard represented by FIXM to reflect the content requirements of a
particular message exchange. Templates offer message-specific guidance
and validation rules while remaining entirely compliant with the broader
FIXM structures.

A list of benefits for employing templates is detailed below.

| **Benefit of templates**     | **Without templates**                                                                                                                                                                        | **With templates**                                                                                                             |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Reduced Development Overhead | Increased development overhead as each user must independently interpret how message content requirements should be represented in FIXM format.                                              | Tailored schemas reduce development overhead by providing additional guidance for creating messages with a FIXM-based content. |
| Consistent Message Structure | Individual interpretations of requirements could lead to inconsistent message content implementation across users.                                                                           | Making dedicated implementation templates available to all users should improve implementation consistency.                    |
| Improved XML Validation      | XML-based validation limited to data syntax checking with no guidance for required vs. optional or allowed vs. not allowed content (failing to fully leverage a major benefit of using XML). | XML-based validation enforces both syntax and content completeness rules (fully leveraging benefits of XML-based validation).  |

The use of message templates therefore improves interoperability, data
quality, and ease and cost of development for any exchange they are
applied to. They provide FIXM users with guidance and structure while at
the same time allowing FIXM to remain open and flexible.

**XML representation of FIXM-based Message Templates**

The XML representation of FIXM-based Message templates is currently
achieved by restricting complex types defined by FIXM. Restricting
complex types is a standard-based approach for removing unwanted
elements and/or attributes and to apply tighter restraints to
multiplicities, patterns, and facets. Complex type restrictions also
provide built-in validation: if the restriction is not correctly formed
in relation to the parent type then the resulting schemas will not
validate.

**Benefits of XSD restrictions**

-   XSD restrictions are explicit: using an XSD schema with restrictions
    means using the rules of the base XSD schema plus additional rules
    that are explicitly declared;

-   XSD restrictions provide some built-in validation for quality
    assurance

-   XSD restrictions represent a natural use of the XSD standard;

-   XSD restrictions deliver benefits in terms of model development and
    maintenance. [3]

**Potential shortcomings of XSD restrictions**

The online literature about XML schema design generally considers that
the restrictions of XSD complex types are the most difficult and
therefore the least supported part of the XML schema specification.
Implementers experiencing issues with the FIXM templates are invited to
report their problems to the FIXM community, with details about the
development environment being used. Alternatives to XSD restrictions may
be then considered, as appropriate (see next section).

**XSD Profiles as a potential alternative to XSD Restrictions**

An XSD profile would represent a reduced, further restricted subset of
the original model. This approach is very similar to using restrictions
but accomplishes the task by directly creating smaller, parallel models
of the adjusted packages rather than producing them via a restriction.
The figure below illustrates at high-level the differences.

<img src=".//media/image7.png" style="width:5.14179in;height:3.52252in" />

<span id="_Toc48643980" class="anchor"></span>Figure 3: XSD Restriction
vs XSD Profile

XSD profiles would not restrict the types from the base reference and
would not bring any additional complexity. They could therefore be
processed by marshalling tools in a smoother way compared to XSD
restrictions.

XSD profiles may be therefore developed as an alternative to XSD
restrictions for representing FIXM-based message templates.

#### How to build an application library?

APPENDIX B provides detailed guidance for creating application
libraries.

### Extensions

#### What is it?

An extension designates a supplement to FIXM that supports additional
(commonly local or regional) requirements from a particular organisation
or community of interest. An extension may supplement FIXM Core by
defining additional flight data structures exchanged locally or
regionally, and/or may supplement an existing Application Library by
defining additional messaging data structure exchanged locally or
regionally.

#### What is a valid use of an extension?

A number of rules are established in order to ensure that extensions are
not developed as a replacement of FIXM Core or a subset thereof.

The requirements on FIXM extensions are provided below. They are equally
applicable to verified and non-verified extensions, but are enforceable
only for verified extension. Non-verified extensions satisfying the
requirements below will be recognised as a valid usage of the FIXM
extension mechanism.

**Requirement on extension design**

| **Requirement**       | To qualify for a valid FIXM extension, an extension shall be designed in accordance with the modelling principles described in APPENDIX A.                                                                                                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Rationale**         | The successful development of an extension, and its successful integration with the FIXM core packages, requires rules on extension design to be followed consistently by all implementers.                                                                                                                      |
| **How to check this** | Checking that an extension satisfies this requirement cannot be automated and requires manual analysis of the extension content by the FIXM community. As a general principle, extensions to FIXM core that are proposed for online publication on the FIXM web site should be checked against this requirement. |

**Requirement on extension content**

| **Requirement**       | To qualify as a valid FIXM extension, an extension shall never contain a model element that would redefine, or supersede, a model element that is already defined in FIXM Core.                                                                                                                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Rationale**         | FIXM core is an information exchange model capturing flight information that is globally harmonised. Redefining or superseding the FIXM core content in an extension would amount to diverging from this globally harmonised content and would go against the fundamental harmonisation objectives of FF-ICE and FIXM. |
| **How to check this** | Checking that an extension satisfies this requirement cannot be automated and requires manual analysis of the extension content by the FIXM community. As a general principle, extensions to FIXM core that are proposed for online publication on the FIXM web site should be checked against this requirement.       |

Example of FIXM extension satisfying the requirement on extension
content

<img src=".//media/image2.png" style="width:0.26042in;height:0.26042in" /><img src=".//media/image8.emf" style="width:5.12598in;height:2.54783in" />

<span id="_Toc48643981" class="anchor"></span>Figure 4: Example of FIXM
extension satisfying the requirement on extension content

This example is an extract from the US NAS extension to FIXM 4.1.0 \[7\]
- Copyright (c) US Federal Aviation Administration (FAA), available on
[www.FIXM.aero](http://www.FIXM.aero). This extract features a class
named “NasFlight” (in blue on the diagram) that extends the core model
element “Extension” and which defines a content that supplements the
core model element “Flight”. The content of class “NasFlight” does not
replace or supersede any of the existing properties of the core “Flight”
class. The example therefore qualifies as valid usage of the extension
mechanism.

Example of FIXM extension NOT satisfying the requirement on extension
content

<img src=".//media/image3.png" style="width:0.2955in;height:0.2955in" /><img src=".//media/image9.png" style="width:4.70091in;height:2.96439in" />

<span id="_Toc48643982" class="anchor"></span>Figure 5: Example of FIXM
extension NOT satisfying the requirement on extension content

This example features a fictitious extension to FIXM Core which models
one class entitled “WrongFlight” (in blue on the diagram). This class
defines a property named “gufi” that is typed using CharacterString. The
extension essentially redefines the “gufi” property from the FIXM core
model element “Flight” and loosens its format, allowing any type of
character string to be populated. This is an example of a FIXM extension
redefining content from FIXM Core. It does NOT qualify as valid usage of
the FIXM extension mechanism.

#### How to build an extension?

The FIXM extension mechanism distributes class-specific extension hooks
throughout the model that implementers can leverage to define their
specific data structures.

<img src=".//media/image10.emf" style="width:6.10435in;height:1.4087in" />

The key benefits of the approach are the following:

1.  ability to allow Extension validation

2.  multiple co-existing Extensions

3.  co-location of Extension data with the Core data it extends

4.  ability to easily remove extensions and pare down the model

This permissive approach enables FIXM users to enrich the core FIXM
datasets with as many information elements as necessary, as required by
the applicable implementation context.

APPENDIX A provides a rulebook and detailed guidance for creating
extensions.

#### Ignoring extension data 

Consumers of FIXM information may not need, and/or may not be able to
process and interpret extension data supplementing a core FIXM dataset.

Using XSLTs is one approach for removing unwanted Extension data (known
or unknown) from a FIXM XML dataset, as appropriate. An example of an
XSLT that removes all Extension content is provided below:

&lt;?xml version="1.0" encoding="UTF-8"?&gt;  
&lt;xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;  
&lt;xsl:output method="xml" version="1.0" encoding="UTF-8"
indent="yes"/&gt;  
&lt;xsl:template match="@\*\|node()"&gt;  
&lt;xsl:copy&gt;  
&lt;xsl:apply-templates select="@\*\|node()"/&gt;  
&lt;/xsl:copy&gt;  
&lt;/xsl:template&gt;  
&lt;xsl:template match="\*:extension"/&gt;  
&lt;/xsl:stylesheet&gt;

