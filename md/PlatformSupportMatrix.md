## Platform Support Matrix

FIXM does not manage the software listed below .This list of tools is
provided for convenience.

<table>
<thead>
<tr class="header">
<th><strong>Purpose</strong></th>
<th><strong>Name</strong></th>
<th><strong>Version</strong></th>
<th><strong>Links</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIXM Schemas</td>
<td>FIXM Core</td>
<td>4.2.0</td>
<td><a href="https://www.fixm.aero/release.pl?rel=FIXM-4.2.0">https://www.fixm.aero/release.pl?rel=FIXM-4.2.0</a></td>
</tr>
<tr class="even">
<td></td>
<td>FF-ICE Message</td>
<td>1.0.0</td>
<td><a href="https://www.fixm.aero/release.pl?rel=FFICE-Msg-1.0.0">https://www.fixm.aero/release.pl?rel=FFICE-Msg-1.0.0</a></td>
</tr>
<tr class="odd">
<td>Java</td>
<td>Java JDK</td>
<td>1.8</td>
<td><a href="https://www.oracle.com/java/technologies/javase-jdk8-downloads.html"><u>https://www.oracle.com/java/technologies/javase-jdk8-downloads.html</u></a></td>
</tr>
<tr class="even">
<td>Operating System</td>
<td><p>Windows Server</p>
<p><em>using Java JDK 1.8</em></p></td>
<td>10</td>
<td></td>
</tr>
<tr class="odd">
<td>Web Server</td>
<td><p>Apache Tomcat</p>
<p><em>using Java JDK 1.8</em></p></td>
<td>8.5.49</td>
<td><a href="https://tomcat.apache.org/download-80.cgi"><u>https://tomcat.apache.org/download-80.cgi</u></a></td>
</tr>
<tr class="even">
<td>IDE</td>
<td><p>IntelliJ</p>
<p><em>using Java JDK 1.8</em></p></td>
<td>2020.1.1</td>
<td><a href="https://www.jetbrains.com/idea/download/#section=windows"><u>https://www.jetbrains.com/idea/download/#section=windows</u></a></td>
</tr>
<tr class="odd">
<td>Data Binding Options</td>
<td>ADP</td>
<td>Axis1</td>
<td>n/a</td>
</tr>
<tr class="even">
<td></td>
<td>JAXBRI</td>
<td><p>Axis1</p>
<p>Axis2</p></td>
<td><a href="http://axis.apache.org/axis2/java/core/download.cgi">http://axis.apache.org/axis2/java/core/download.cgi</a></td>
</tr>
<tr class="odd">
<td>Code Generation</td>
<td>WSDL2Java</td>
<td>Axis2 Version 1.7.9</td>
<td><a href="https://axis.apache.org/axis2/java/core/docs/quickstartguide.html"><u>https://axis.apache.org/axis2/java/core/docs/quickstartguide.html</u></a></td>
</tr>
<tr class="even">
<td>Build</td>
<td>Apache Ant</td>
<td>1.10.7</td>
<td><a href="https://ant.apache.org/bindownload.cgi"><u>https://ant.apache.org/bindownload.cgi</u></a></td>
</tr>
<tr class="odd">
<td>API Testing T</td>
<td>Postman</td>
<td>7.23</td>
<td><a href="https://www.postman.com/downloads/"><u>https://www.postman.com/downloads/</u></a></td>
</tr>
<tr class="even">
<td></td>
<td>SoapUI</td>
<td>5.5.0</td>
<td><a href="https://www.soapui.org/downloads/soapui.html"><u>https://www.soapui.org/downloads/soapui.html</u></a></td>
</tr>
</tbody>
</table>


The following outlines the steps to build a basic FIXM web service.

<img src=".//media/image250.png" style="width:7.68472in;height:4.1875in" />

1.  <span id="_Toc48643928" class="anchor"></span>**Generate
    JAXB-RI-Bound Source Code**

> Execute the WSDL2Java command (from the command-line)
>
> <img src=".//media/image251.png" style="width:6.06335in;height:2.1253in" />
>
> Successful execution results in the generation of:

-   A receiving stub, which contains a code skeleton for receiving a
    > submitted flight plan. All business logic for your project should
    > be within the calling scope of the skeleton.

-   A well-defined Flight Plan response model that the skeleton code
    > returns.

-   The file Build.xml (ANT tool uses this).

1.  **Add additional logic**

> Add additional client code and server-side business logic to implement
> the services, which the web service needs to function. **Note**: The
> generated-code will compile but will fail with Exceptions. Additional
> programming is required.

1.  **Build and Deploy Server Code**

> Issue the following command to compile the entire source code. Ant
> will package the service as an ‘aar’ file and deploy it to the Axis
> service folder running under tomcat.
>
> <img src=".//media/image252.png" style="width:0.83345in;height:0.28129in" />

1.  **Start Tomcat Server**

To start Tomcat server run the following command that is located in the
%CATALINA\_HOME %/bin directory.

> > <img src=".//media/image253.png" style="width:0.9793in;height:0.31254in" />

1.  **List Services**

> List the services provided by the web service. The expected services
> will be listed under “Available services”.
>
> <http://localhost:8080/axis2/services/listServices>.

1.  **Verify Running Services**

> Obtain the WSDL from the service to verify that the service is running
> and able to accept requests

<http://localhost:8080/axis2/services/FlightPlanningService?wsdl>


#### Mapping of ATS Fields to FIXM

This section provides a mapping from fields in PANS-ATM ATS messages to
the FIXM Logical Model, one ATS message field per subsection. The
columns in the mapping tables are defined in Table 8.

<span id="_Toc48644031" class="anchor"></span>Table 8: Column
Definitions

| **Column**       | **Description**                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| PANS-ATM Field   | The field number as defined in ICAO Doc 4444 \[PANS-ATM\].                                                                                          |
| Package          | The package that contains the definition of the PANS-ATM field in the logical model.                                                                |
| Class            | The class (in the specified package) that models the PANS-ATM field.                                                                                |
| Path from Flight | Starting from class *Flight* in package *Flight.FlightData*, this defines the path to the location in the logical model where the field is encoded. |

Table 9 provides an explanation of an entry in the map using the flight
identifier recorded in field 7a of an ICAO ATS message (section Field
7).

<span id="_Toc48644032" class="anchor"></span>Table 9: Example

| Column           | Value                                       | Description                                                                                                                                                                                                          |
|------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PANS-ATM Field   | 7a                                          | This is the field number from PANS-ATM that represents the flight identifier, which is being mapped to the logical model.                                                                                            |
| Package          | Base.Types                                  | The flight identifier is modelled in the *Base.Types* package.                                                                                                                                                       |
| Class            | AircraftIdentification                      | The name of the class that models a flight identifier is *AircraftIdentification*.                                                                                                                                   |
| Path from Flight | flightIdentification.aircraftIdentification | Starting at class *Flight*, follow the *flightIdentification* association to class *FlightIdentification*, then to the *aircraftIdentification* attribute of that class (which is of type *AircraftIdentification*). |

A PANS-ATM ATS message field may be mapped to different FIXM elements
depending on context. A simple constraint notation based on logic and
set theory is employed to specify these conditions. The notation is
described in Table 10.

<span id="_Toc48644033" class="anchor"></span>Table 10: Constraint
Notation

| Notation      | Description                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| \[ . . . . \] | A constraint. The field in question is only encoded in the specified FIXM element if the constraint is satisfied. |
| A ∧ B         | Logical conjunction: both A and B are true.                                                                       |
| A ∨ B         | Logical disjunction: A is true or B is true.                                                                      |
| A = B         | Equality: A and B are equal.                                                                                      |
| A ≠ B         | Inequality: A and B are not equal.                                                                                |
| A ∈ B         | Set membership: the item A is contained in the set/list B.                                                        |
| A ∉ B         | Set exclusion: the item A is not contained in the set/list B.                                                     |
| Free text     | If the constraint is not amenable to formal specification, it is described in text.                               |

The term ‘〈kind〉’ in the subsequent tables (fields 8, 13, 15, 16 and
18) is a reference to the kind of route/trajectory information to which
a field is mapped. That route information is dependent on the message
type. Refer to section Varieties of Route for a mapping between the
message type and the kind of route information.

##### Field 3

Field 3 in an ATS message denotes the message type. FIXM is concerned
with modelling information that may be included in a message, but FIXM
itself does not define messages (section **Error! Reference source not
found.**). As such, there is no equivalent of ATS field 3 in FIXM.

##### Field 5

| ICAO 4444 Field | Package          | Class           | Path from Flight                            |
|-----------------|------------------|-----------------|---------------------------------------------|
| 5a              | Flight.Emergency | EmergencyPhase  | emergency.phase                             |
| 5b              | Base.Types       | TextName        | emergency.originator.atcUnitNameOrAlternate |
| 5c              | Base.Types       | CharacterString | emergency.emergencyDescription              |

##### Field 7

| ICAO 4444 Field | Package    | Class                  | Path from Flight                            |
|-----------------|------------|------------------------|---------------------------------------------|
| 7a              | Base.Types | AircraftIdentification | flightIdentification.aircraftIdentification |
| 7b/c            | Base.Types | ModeACode              | enRoute.currentModeACode                    |

##### Field 8

| ICAO 4444 Field | Package                                      | Class               | Path from Flight                                                   |
|-----------------|----------------------------------------------|---------------------|--------------------------------------------------------------------|
| 8a              | Flight.FlightRouteTrajectory.RouteTrajectory | FlightRulesCategory | routeTrajectoryGroup.〈kind〉.routeInformation.flightRulesCategory |
| 8b              | Flight.FlightData                            | TypeOfFlight        | flightType                                                         |

##### Field 9

<table>
<thead>
<tr class="header">
<th>ICAO 4444 Field</th>
<th>Package</th>
<th>Class</th>
<th>Path from Flight</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9a</td>
<td>Base.Types</td>
<td>Count</td>
<td><p>aircraft.formationCount</p>
<p>If the FIXM number of aircraft is greater than 99, set field 9a to 99.</p></td>
</tr>
<tr class="even">
<td>9b</td>
<td>Base.Types</td>
<td>AircraftTypeDesignator</td>
<td><p>[9b≠ZZZZ]</p>
<p>aircraft.aircraftType.type.icaoAircraftTypeDesignator</p></td>
</tr>
<tr class="odd">
<td>9c</td>
<td>Flight.Aircraft</td>
<td>WakeTurbulenceCategory</td>
<td>aircraft.wakeTurbulence</td>
</tr>
</tbody>
</table>

##### Field 10

| ICAO 4444 Field | Package           | Class                               | Path from Flight                                                        |
|-----------------|-------------------|-------------------------------------|-------------------------------------------------------------------------|
| 10a             | Flight.Capability | StandardCapabilitiesIndicator       | aircraft.capabilities.standardCapabilities                              |
|                 |                   | CommunicationCapabilityCode         | aircraft.capabilities.communication.communicationCapabilityCode         |
|                 |                   | DatalinkCommunicationCapabilityCode | aircraft.capabilities.communication.datalinkCommunicationCapabilityCode |
|                 |                   | NavigationCapabilityCode            | aircraft.capabilities.navigation.navigationCapabilityCode               |
| 10b             | Flight.Capability | SurveillanceCapabilityCode          | aircraft.capabilities.surveillance.surveillanceCapabilityCode           |

##### Field 13

<table>
<thead>
<tr class="header">
<th>ICAO 4444 Field</th>
<th>Package</th>
<th>Class</th>
<th>Path from Flight</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>13a</td>
<td>Base.Organization</td>
<td>LocationIndicator</td>
<td><p>[13a≠AFIL ∧ 13a≠ZZZZ]</p>
<p>departure.aerodrome.locationIndicator</p></td>
</tr>
<tr class="even">
<td></td>
<td>Flight.Departure</td>
<td>AirfileIndicator</td>
<td><p>[13a=AFIL]</p>
<p>departure.airfileIndicator = AIRFILE</p></td>
</tr>
<tr class="odd">
<td>13b</td>
<td>Base.Types</td>
<td>Time</td>
<td><p>[13a≠AFIL ∧ message∈{FPL,ARR,CHG,CNL,DLA,RQS,RQP}]</p>
<p>departure.estimatedOffBlockTime</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><p>[13a≠AFIL ∧ message∈{ALR,DEP,SPL}]</p>
<p>departure.actualTimeOfDeparture</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><p>[13a=AFIL]</p>
<p>routeTrajectoryGroup.〈kind〉.routeInformation.airfileRouteStartTime</p></td>
</tr>
</tbody>
</table>

##### Field 14

| ICAO 4444 Field | Package                    | Class                       | Path from Flight                                                            |
|-----------------|----------------------------|-----------------------------|-----------------------------------------------------------------------------|
| 14a             | Base.AeronauticalReference | SignificantPointChoice      | enroute.boundaryCrossingCoordination.crossingPoint                          |
| 14b             | Base.Types                 | Time                        | enroute.boundaryCrossingCoordination.crossingTime                           |
| 14c             | Base.RangesAndChoices      | FlightLevelOrAltitudeChoice | enroute.boundaryCrossingCoordination.clearedLevel                           |
| 14d             | Flight.EnRoute             | FlightLevelOrAltitudeChoice | enroute.boundaryCrossingCoordination.altitudeInTransition.level             |
| 14e             | Flight.EnRoute             | BoundaryCrossingCondition   | enroute.boundaryCrossingCoordination.altitudeInTransition.crossingCondition |

##### Field 15

<table>
<thead>
<tr class="header">
<th>ICAO 4444 Field</th>
<th>Package</th>
<th>Class</th>
<th>Path from Flight</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15a</td>
<td>Base.Measures</td>
<td>TrueAirspeed</td>
<td>routeTrajectoryGroup.〈kind〉.routeInformation.cruisingSpeed</td>
</tr>
<tr class="even">
<td>15b</td>
<td>Base.RangesAndChoices</td>
<td>FlightLevelOrAltitudeChoice</td>
<td><p>[15b≠VFR]</p>
<p>routeTrajectoryGroup.〈kind〉.routeInformation.cruisingLevel</p></td>
</tr>
<tr class="odd">
<td>15c</td>
<td>Flight.FlightRouteTrajectory.RouteTrajectory</td>
<td>RouteTrajectoryElement</td>
<td>routeTrajectoryGroup.〈kind〉.element</td>
</tr>
<tr class="even">
<td></td>
<td>Base.Types</td>
<td>CharacterString</td>
<td>routeTrajectoryGroup.〈kind〉.routeInformation.routeText</td>
</tr>
<tr class="odd">
<td>15c1</td>
<td>Base.AeronauticalReference</td>
<td>SidStarReference</td>
<td>routeTrajectoryGroup.〈kind〉.element.routeDesignatorToNextElement.standardInstrumentDeparture</td>
</tr>
<tr class="even">
<td>15c2</td>
<td>Base.AeronauticalReference</td>
<td>RouteDesignator</td>
<td>routeTrajectoryGroup.〈kind〉.element.routeDesignatorToNextElement.routeDesignator</td>
</tr>
<tr class="odd">
<td>15c3</td>
<td>Base.AeronauticalReference</td>
<td>SignificantPointChoice</td>
<td>routeTrajectoryGroup.〈kind〉.element.elementStartPoint</td>
</tr>
<tr class="even">
<td>15c4</td>
<td>Base.AeronauticalReference</td>
<td>SignificantPointChoice</td>
<td>routeTrajectoryGroup.〈kind〉.element.elementStartPoint</td>
</tr>
<tr class="odd">
<td></td>
<td>Base.Measures</td>
<td>TrueAirspeed</td>
<td>routeTrajectoryGroup.〈kind〉.element.routeChange.speed.speed</td>
</tr>
<tr class="even">
<td></td>
<td>Base.RangesAndChoices</td>
<td>FlightLevelOrAltitudeChoice</td>
<td>routeTrajectoryGroup.〈kind〉.element.routeChange.level.level</td>
</tr>
<tr class="odd">
<td>15c5</td>
<td>Flight.FlightRouteTrajectory.RouteTrajectory</td>
<td>FlightRules</td>
<td><p>[15c5=IFR ∨ 15c5=VFR]</p>
<p>routeTrajectoryGroup.〈kind〉.element.flightRulesChange</p></td>
</tr>
<tr class="even">
<td></td>
<td>Flight.FlightRouteTrajectory.RouteTrajectory</td>
<td>OtherRouteDesignator</td>
<td><p>[15c5=DCT]</p>
<p>routeTrajectoryGroup.〈kind〉.element.routeDesignatorToNextElement.otherRouteDesignator = DIRECT</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Flight.FlightRouteTrajectory.RouteTrajectory</td>
<td>RouteTruncationIndicator</td>
<td><p>[15c5=T]</p>
<p>routeTrajectoryGroup.〈kind〉.element.routeTruncationIndicator = ROUTE_TRUNCATION</p></td>
</tr>
<tr class="even">
<td>15c6</td>
<td>Base.AeronauticalReference</td>
<td>SignificantPointChoice</td>
<td>routeTrajectoryGroup.〈kind〉.element.elementStartPoint</td>
</tr>
<tr class="odd">
<td></td>
<td>Base.Measures</td>
<td>TrueAirspeed</td>
<td>routeTrajectoryGroup.〈kind〉.element.routeChange.cruiseClimbStart.speed</td>
</tr>
<tr class="even">
<td></td>
<td>Base.RangesAndChoices</td>
<td>VerticalRange</td>
<td><p>[PLUS∉15c6]</p>
<p>routeTrajectoryGroup.〈kind〉.element.routeChange.cruiseClimbStart.level.flightLevelOrAltitudeRange</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Base.RangesAndChoices</td>
<td>FlightLevelOrAltitudeChoice</td>
<td><p>[PLUS∈15c6]</p>
<p>routeTrajectoryGroup.〈kind〉.element.routeChange.cruiseClimbStart.level.flightLevelOrAltitudeValue</p></td>
</tr>
<tr class="even">
<td>15c7</td>
<td>Base.AeronauticalReference</td>
<td>SidStarReference</td>
<td>routeTrajectoryGroup.〈kind〉.element.routeDesignatorToNextElement.standardInstrumentArrival</td>
</tr>
</tbody>
</table>

##### Field 16

<table>
<thead>
<tr class="header">
<th>ICAO 4444 Field</th>
<th>Package</th>
<th>Class</th>
<th>Path from Flight</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>16a</td>
<td>Base.Organization</td>
<td>LocationIndicator</td>
<td><p>[16a≠ZZZZ]</p>
<p>arrival.destinationAerodrome.locationIndicator</p></td>
</tr>
<tr class="even">
<td>16b</td>
<td>Base.Types</td>
<td>Duration</td>
<td>routeTrajectoryGroup.〈kind〉.routeInformation.totalEstimatedElapsedTime</td>
</tr>
<tr class="odd">
<td>16c</td>
<td>Base.Organization</td>
<td>LocationIndicator</td>
<td><p>[16c≠ZZZZ]</p>
<p>arrival.destinationAerodromeAlternate.locationIndicator</p>
<p>If there are more than two FIXM destination alternates, only the first two are used when translating to field 16c.</p></td>
</tr>
</tbody>
</table>

##### Field 17

<table>
<thead>
<tr class="header">
<th>ICAO 4444 Field</th>
<th>Package</th>
<th>Class</th>
<th>Path from Flight</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>17a</td>
<td>Base.Organization</td>
<td>LocationIndicator</td>
<td><p>[17a≠ZZZZ]</p>
<p>arrival.arrivalAerodrome.locationIndicator</p></td>
</tr>
<tr class="even">
<td>17b</td>
<td>Base.Types</td>
<td>Time</td>
<td>arrival.actualTimeOfArrival</td>
</tr>
<tr class="odd">
<td>17c</td>
<td>Base.Aerodrome</td>
<td>AerodromeName</td>
<td><p>[17a=ZZZZ]</p>
<p>arrival.arrivalAerodrome.name</p></td>
</tr>
</tbody>
</table>

##### Field 18

<table>
<thead>
<tr class="header">
<th>ICAO 4444 Field</th>
<th>Package</th>
<th>Class</th>
<th>Path from Flight</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STS</td>
<td>Flight.FlightData</td>
<td>SpecialHandlingReasonCode</td>
<td>specialHandling</td>
</tr>
<tr class="even">
<td>PBN</td>
<td>Flight.Capability</td>
<td>PerformanceBasedNavigationCapabilityCode</td>
<td><p>[R∈10a]</p>
<p>aircraft.capabilities.navigation.performanceBasedCode</p>
<p>If there are more than eight FIXM PBN codes, apply the rules defined in FF-ICE Implementation Guidance section 13.2.2 s) when translating to field 18 PBN.</p></td>
</tr>
<tr class="odd">
<td>NAV</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td><p>[Z∈10a]</p>
<p>aircraft.capabilities.navigation.otherNavigationCapabilities</p></td>
</tr>
<tr class="even">
<td>COM</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td><p>[Z∈10a]</p>
<p>aircraft.capabilities.communication.otherCommunicationCapabilities</p></td>
</tr>
<tr class="odd">
<td>DAT</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td><p>[Z∈10a]</p>
<p>aircraft.capabilities.communication.otherDatalinkCapabilities</p></td>
</tr>
<tr class="even">
<td>SUR</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td>aircraft.capabilities.surveillance.otherSurveillanceCapabilities</td>
</tr>
<tr class="odd">
<td>DEP</td>
<td>Base.Aerodrome</td>
<td>AerodromeReference</td>
<td><p>[13a=ZZZZ]</p>
<p>departure.aerodrome.name</p>
<p>departure.aerodrome.referencePoint</p></td>
</tr>
<tr class="even">
<td></td>
<td>Base.Types</td>
<td>TextName</td>
<td><p>[13a=AFIL]</p>
<p>flightPlanSubmitter.name</p></td>
</tr>
<tr class="odd">
<td>DEST</td>
<td>Base.Aerodrome</td>
<td>AerodromeReference</td>
<td><p>[16a=ZZZZ]</p>
<p>destination.destinationAerodrome.name</p>
<p>destination.destinationAerodrome.referencePoint</p></td>
</tr>
<tr class="even">
<td>DOF</td>
<td>Base.Types</td>
<td>Time</td>
<td><p>[13a≠AFIL]</p>
<p>departure.estimatedOffBlockTime</p>
<p>[13a=AFIL]</p>
<p>routeTrajectoryGroup.〈kind〉.route.airfileRouteStartTime</p>
<p>Note: DOF is not modelled as a distinct attribute in FIXM, it is a component of the departure or air filed start date/time (see field 13b on page 111)</p></td>
</tr>
<tr class="odd">
<td>REG</td>
<td>Flight.Aircraft</td>
<td>AircraftRegistration</td>
<td><p>aircraft.registration</p>
<p>If there is more than one FIXM registration, insert the first only in field 18 REG.</p></td>
</tr>
<tr class="even">
<td>EET</td>
<td>Base.AeronauticalReference</td>
<td>AirspaceDesignator</td>
<td><p>[Airspace boundary specified]</p>
<p>routeTrajectoryGroup.〈kind〉.routeInformation.estimatedElapsedTime.location.region</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Base.AeronauticalReference</td>
<td>SignificantPointChoice</td>
<td><p>[Significant point specified]</p>
<p>routeTrajectoryGroup.〈kind〉.routeInformation.estimatedElapsedTime.location.point</p></td>
</tr>
<tr class="even">
<td></td>
<td>Base.AeronauticalReference</td>
<td>Longitude</td>
<td><p>[Longitude specified]</p>
<p>routeTrajectoryGroup.〈kind〉.routeInformation.estimatedElapsedTime.location.longitude</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Base.Types</td>
<td>Duration</td>
<td>routeTrajectoryGroup.〈kind〉.routeInformation.estimatedElapsedTime.elapsedTime</td>
</tr>
<tr class="even">
<td>SEL</td>
<td>Flight.Capability</td>
<td>SelectiveCallingCode</td>
<td>aircraft.capabilities.communication.selectiveCallingCode</td>
</tr>
<tr class="odd">
<td>TYP</td>
<td>Base.Types</td>
<td>Count</td>
<td><p>[9b=ZZZZ]</p>
<p>aircraft.aircraftType.numberOfAircraft</p></td>
</tr>
<tr class="even">
<td></td>
<td>Base.Types</td>
<td>CharacterString</td>
<td><p>[9b=ZZZZ]</p>
<p>aircraft.aircraftType.type.otherAircraftType</p></td>
</tr>
<tr class="odd">
<td>CODE</td>
<td>Flight.Aircraft</td>
<td>AircraftAddress</td>
<td>aircraft.aircraftAddress</td>
</tr>
<tr class="even">
<td>DLE</td>
<td>Base.AeronauticalReference</td>
<td>SignificantPoint</td>
<td>routeTrajectoryGroup.〈kind〉.element.elementStartPoint (see also field 15c3, 15c4 and 15c6)</td>
</tr>
<tr class="odd">
<td></td>
<td>Base.Types</td>
<td>Duration</td>
<td>routeTrajectoryGroup.〈kind〉.element.enRouteDelay.delayValue</td>
</tr>
<tr class="even">
<td>OPR</td>
<td>Base.Organization</td>
<td>AircraftOperatorDesignator</td>
<td><p>[ICAO designator specified]</p>
<p>operator.designatorIcao</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Base.Types</td>
<td>TextName</td>
<td><p>[ICAO designator not specified]</p>
<p>operator.operatingOrganization.name</p></td>
</tr>
<tr class="even">
<td>ORGN</td>
<td>Base.Types</td>
<td>TextName</td>
<td>flightPlanOriginator.name</td>
</tr>
<tr class="odd">
<td>PER</td>
<td>Flight.Aircraft</td>
<td>AircraftApproachCategory</td>
<td>aircraft.aircraftApproachCategory</td>
</tr>
<tr class="even">
<td>ALTN</td>
<td>Base.Aerodrome</td>
<td>OtherReference</td>
<td><p>[ZZZZ∈16c]</p>
<p>arrival.destinationAerodromeAlternate.name</p>
<p>arrival.destinationAerodromeAlternate.referencePoint</p></td>
</tr>
<tr class="odd">
<td>RALT</td>
<td>Base.Aerodrome</td>
<td>AerodromeReference</td>
<td>enRoute.alternateAerodrome</td>
</tr>
<tr class="even">
<td>TALT</td>
<td>Base.Aerodrome</td>
<td>AerodromeReference</td>
<td>departure.takeOffAlternateAerodrome</td>
</tr>
<tr class="odd">
<td>RIF</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td>arrival.reclearanceInFlight.routeToRevisedDestination</td>
</tr>
<tr class="even">
<td></td>
<td>Base.Aerodrome</td>
<td>AerodromeReference</td>
<td>arrival.reclearanceInFlight.filedRevisedDestinationAerodrome</td>
</tr>
<tr class="odd">
<td>RMK</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td>remarks</td>
</tr>
</tbody>
</table>

##### Field 19

| ICAO 4444 Field | Package           | Class                        | Path from Flight                                               |
|-----------------|-------------------|------------------------------|----------------------------------------------------------------|
| 19a             | Base.Types        | Duration                     | supplementaryData.fuelEndurance                                |
| 19b             | Base.Types        | Count                        | supplementaryData.personsOnBoard                               |
| 19c             | Flight.Capability | EmergencyRadioCapabilityType | aircraft.capabilities.survival.emergencyRadioCapabilityType    |
| 19d             | Flight.Capability | SurvivalEquipmentType        | aircraft.capabilities.survival.survivalEquipmentType           |
| 19e             | Flight.Capability | LifeJacketType               | aircraft.capabilities.survival.lifeJacketType                  |
| 19f             | Base.Types        | Count                        | aircraft.capabilities.survival.dinghyInformation.number        |
|                 | Base.Types        | Count                        | aircraft.capabilities.survival.dinghyInformation.totalCapacity |
|                 | Flight.Capability | DinghyCoverIndicator         | aircraft.capabilities.survival.dinghyInformation.covered       |
|                 | Base.Types        | CharacterString              | aircraft.capabilities.survival.dinghyInformation.colour        |
| 19g             | Base.Types        | CharacterString              | aircraft.coloursAndMarkings                                    |
|                 | ~~Base.Types~~    | ~~CharacterString~~          | ~~aircraft.significantMarkings~~                               |
| 19h             | Base.Types        | CharacterString              | aircraft.capabilities.survival.survivalEquipmentRemarks        |
| 19i             | Base.Types        | TextName                     | supplementaryData.pilotInCommand.name                          |

##### Field 20

<table>
<thead>
<tr class="header">
<th>ICAO 4444 Field</th>
<th>Package</th>
<th>Class</th>
<th>Path from Flight</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>20a<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>Base.Organization</td>
<td>AircraftOperatorDesignator</td>
<td><p>[ICAO designator specified]</p>
<p>operator.designatorIcao</p></td>
</tr>
<tr class="even">
<td></td>
<td>Base.Types</td>
<td>TextName</td>
<td><p>[ICAO designator not specified]</p>
<p>operator.operatingOrganization.name</p></td>
</tr>
<tr class="odd">
<td>20b</td>
<td>Base.AeronauticalReference</td>
<td>AtcUnitName</td>
<td>emergency.lastContact.lastContactUnit</td>
</tr>
<tr class="even">
<td>20c</td>
<td>Base.Types</td>
<td>Time</td>
<td>emergency.lastContact.lastContactTime</td>
</tr>
<tr class="odd">
<td>20d</td>
<td>Base.Measures</td>
<td>Frequency</td>
<td>emergency.lastContact.lastContactFrequency</td>
</tr>
<tr class="even">
<td>20e</td>
<td>Base.AeronauticalReference</td>
<td>SignificantPointChoice</td>
<td>emergency.lastContact.position.position</td>
</tr>
<tr class="odd">
<td></td>
<td>Base.Types</td>
<td>Time</td>
<td>emergency.lastContact.position.timeAtPosition</td>
</tr>
<tr class="even">
<td>20f</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td>emergency.lastContact.position.determinationMethod</td>
</tr>
<tr class="odd">
<td>20g</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td>emergency.actionTaken</td>
</tr>
<tr class="even">
<td>20h</td>
<td>Base.Types</td>
<td>CharacterString</td>
<td>emergency.otherInformation</td>
</tr>
</tbody>
</table>
<section class="footnotes" role="doc-endnotes">
<hr />
<ol>
<li id="fn1" role="doc-endnote"><p>Field 20a maps to the same FIXM field as field 18 OPR. An ALR can include field 18 and field 20 with potentially conflicting values. Further consideration of this is required.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

##### Field 21

| ICAO 4444 Field | Package                    | Class                  | Path from Flight                                          |
|-----------------|----------------------------|------------------------|-----------------------------------------------------------|
| 21a             | Base.Types                 | Time                   | radioCommunicationFailure.contact.lastContactTime         |
| 21b             | Base.Measures              | Frequency              | radioCommunicationFailure.contact.lastContactFrequency    |
| 21c             | Base.AeronauticalReference | SignificantPointChoice | radioCommunicationFailure.contact.position.position       |
| 21d             | Base.Types                 | Time                   | radioCommunicationFailure.contact.position.timeAtPosition |
| 21e             | Base.Types                 | CharacterString        | radioCommunicationFailure.remainingComCapability          |
| 21f             | Base.Types                 | CharacterString        | radioCommunicationFailure.radioFailureRemarks             |

##### Field 22

In an ATS message, field 22 specifies a change to the information
associated with a flight. It does not define new information elements,
just a modification to elements that appear in other fields. As such,
there are no mapping rules for field 22. The mapping of the information
that can be specified in field 22 is captured in the other fields. For
example, the entry *-7/NEWACID* in field 22 has the same mapping as if
*–NEWACID* appeared in field 7 (on page 110).

[1] To do so, FIXM has transitioned from attributes to allowing for the
model-wide support of “nillable” properties.

[2] They should not, however, include any additional flight data
structures needed to support the specific data exchange. If such fields
are required, they should be supplied via Extensions.

[3] When newer versions of FIXM products are released, upgrading the
restrictions only requires updating the reference to the newer versions
and implementing the ad-hoc adaptations only for the parts that have
changed.

[4] FIXM does not use GML but mimics it for geographic positions. GML
encodes geographic locations as sequences of values since it employs the
same construct to represent polygons.

[5] This design is intentional. It saves FIXM from being tied to an
external standard for such a small use case and also aims to avoid
potential issues or difficulties when marshalling / unmarshalling the
standard xlink:href attribute.

[6] From draft Volume I of the ICAO Manual on SWIM (ICAO Doc 10039)

[7] See chapter 2.2.2 for a general introduction to the concept of
Application Library.

[8] ***Publication Service***, ***Trial Service and Notification
Service*** are not covered by this example.

[9] See in particular \[10\], Section 2.3.2, Figure 1

[10] Web Service Operations are used to couple a request and a reply.
Service operations indicate the intent or the results of the information
exchange.

[11] It is assumed that validation of the flight plan ensures when code
‘N’ is included in field 10a, no other code is included, but such
validation is not part of the translation rules.

[12] It is assumed that validation of the flight plan ensures the field
10a code ‘R’ is always paired with field 18 PBN, but such validation is
not part of the translation rules.

[13] It is assumed that validation of the flight plan ensures the field
10a code ‘Z’ is always paired with at least one of field 18 NAV, COM or
DAT, but such validation is not part of the translation rules.

[14] It is assumed that validation of the flight plan ensures when code
‘N’ is included in field 10b, no other code is included, but such
validation is not part of the translation rules.

[15] If field 18 DOF is omitted it is necessary to apply business rules
to calculate the date of flight. Such business rules are outside the
scope of this chapter. The responsibility lies with individual
stakeholders.

[16] Note that each Extension must target the same version of FIXM Core
and/or Application Library in order to be used together. For example,
you cannot combine one Extension that uses FIXM Core 4.2.0 with another
Extension that uses FIXM Core 4.1.0.

[17] Starting with the Basic Message v1.0.0 model and then deleting the
BasicMessage package allows you to skip creating and setting up the
Applications container and associated schema directory.

[18] The FIXM development team uses Sparx Systems Enterprise Architect
version 13.5, build 1352 for all development work.

[19] Note that a package in Sparx EA can have more than one associated
diagram. To date, FIXM products have only created one diagram per
package, though.

[20] Though FIXM tends to use namespaces that look like URLs, the
namespace value do not need to resolve to an actual location on the
Internet. The namespace is just a field used to resolve naming
collisions between schemas and should, therefore, be distinctive enough
to ensure a reasonably high chance it is not used by another schema.

[21] This example used “xmg” but the prefix can be set to any value that
makes sense in the context of your Application. Because it will be used
throughout your generated schemas, a short prefix is typically
preferred.

[22] If your toolbox is not showing XML Schema options, make sure you’ve
applied the XSDschema stereotype to your package and close and then
reopen the diagram.

[23] Note that position tags may need to be updated appropriately any
time you add, remove, or rename an attribute or association. Be sure to
check your position tags anytime you edit your model.

[24] This is important because XSD complex type restrictions, the
mechanism used to create the templates, must use the same namespace as
the types they restrict. Because of this, different versions of
templates are not able to use distinct namespaces to distinguish
themselves from each other. Tying the versioning of the templates to the
versioning of the Application package and changing that versioning each
time the templates change solves this issue.

[25] Note that these pastes must be performed back to back. If you go
back and re-copy the package after the first paste, any additional
sub-packages added will be copied as well and would then need to be
manually deleted.

[26] Note, this only applies to the package itself – not the contents of
the package. Creating the contents of the message template is covered in
[Create Template Contents](#create-template-content).

[27] XML attributes, rarely used in this version of FIXM, are handled
differently. If you wish to remove an XML attribute from your restricted
class, the field must be retained but the “use” tag associated with the
field must be set to a value of “prohibited”.

[28] If deleted, these associations will be removed entirely from the
model, including Core! It is very important that you <u>do not</u> do
this.

[29] It is important to note that this substitution of a restricted
class for the class it is derived from can also be done for attributes.
If your templates add restrictions to any classes defined in Core’s Base
package, use them when specifying the *Type* field of your attributes as
needed. The FficeMessage templates provide examples of this for the
PersonOrOrganization class.

[30] Don’t forget to create any needed directories outside of Sparx EA
to accommodate your schema structure.

[31] Note that it is very important to explicitly delete any unwanted
connectors. If you instead delete the class in the diagram that the
connector is attached to, this will remove the connector from the
diagram but it will still exist within the model. This can cause
undesired elements to be created when generating the physical model.

[32] The FIXM development team uses Sparx Systems Enterprise Architect
version 13.5, build 1352 for all development work.

[33] Though FIXM tends to use namespaces that look like URLs, the
namespace value do not need to resolve to an actual location on the
Internet. The namespace is just a field used to resolve naming
collisions between schemas and should, therefore, be distinctive enough
to ensure a reasonably high chance it is not used by another schema.

[34] This example used “xmp” but the prefix can be set to any value that
makes sense in the context of your extension. Because it will be used
throughout your generated schemas, a short prefix is typically
preferred.

[35] In FIXM, attributes are standardly used when the field you are
adding is of a Type defined in the Core’s Base package. When defining
your own types, they are standardly attached to a class by using an
association instead. In this example, we will be adding a new field of
type GeographicalPosition from the AeronauticalReference package under
Base so using an attribute is the appropriate choice.

[36] The FIXM development team uses Sparx Systems Enterprise Architect
version 13.5, build 1352 for all development work.

[37] This could be the root package of an entire FIXM product (for
example, the Core package or the FficeMessage package under
Applications) or a particular sub-section or individual sub-package (for
example, the Base package under Core or the EnRoute package under
Flight) of a FIXM product.

[38] This Perl script was developed using perl 5, version 16, subversion
3 (v5.16.3) built for x86\_64-linux-thread-multi and originally tested
in a Linux environment (CentOS Linux 7 (Core)). It was also tested using
perl 5, version 28, subversion 1 (v5.28.1) built for
MSWin32-x64-multi-thread in a Windows environment (Windows 7 Enterprise
(Service Pack 1)).

[39] Sometimes named ***Flight Plan Cancellation Message***

[40] This is commonly known as Request-Reply Message Exchange Pattern.

[41] This is commonly known as Publish-Subscribe Message Exchange
Pattern.

[42] Web Service Operations are used to couple a request and a reply.
Service operations indicate the intent or the results of the information
exchange.
