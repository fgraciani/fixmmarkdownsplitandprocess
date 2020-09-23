## Evaluation Environment

The evaluation process included the following components:

1.  **FIXM Schemas**

    1.  FIXM Core 4.2.0

    2.  FF-ICE Message 1.0.0 (with restrictions)

2.  **WSDL file**

Two WSDL files were tested

1.  The first file contained FIXM schema details that contained no
    restrictions.

2.  The second filed contained FIXM schema details that contained
    restrictions.

<!-- -->

1.  **FlightPlanningService Web Service**

The FIXM test web service being evaluated here is called
*FlightPlanningService*, which supports one operation called
*submitFlightPlan*. Developer can issue a submitFlightPlan remote
request, as either a REST or SOAP call, to the FIXM
*FlightPlanningService* and receive a submission response from the
Service.

> This is a very basic web service to test the sending of minimal flight
> plan XML via SOAP to a server in an attempt to get a web service
> SubmissionResponse. Testing focused mainly on Java based client and
> server.

The below sections will outline the approach and findings associated
with the evaluation of various tools tested in interpreting the Fixm
WSDL file to produce the Fixm server and client Java code.

A number of tools were tested but the Apache Axis library and the
WSDL2Java tool were found to provide the most success.

**<u>Example WSDL (FIXM Schema with Restrictions)</u>**

<img src=".//media/image249.png" style="width:7.375in;height:7.75in" />

