## Message classification and technology selection

FF-ICE/R1 Messages can be classified from the perspective of the
participant who provides the service. Two types of messages can be
identified: input messages and output messages. The input messages are
those received by the service provider while the output messages are
sent by the service provider.

According to the classification above, the FF-ICE/R1 Messages can be
classified as following:

1.  ***Planning Service***

    1.  Input messages:

        1.  ***Preliminary Flight Plan Message***, as specified in
            \[10\] Page II-E-3 Section C-2

        2.  ***Flight Plan Update Message**,* as specified in \[10\]
            Page II-E-19 Section C-9

        3.  ***Flight Cancellation Message***[39] as specified in \[10\]
            Page II-E-17 Section C-8

    2.  Output messages:

        1.  ***Submission Response Message**,* as specified in \[10\]
            Page II-C-1 Section C-1

        2.  ***Planning Status Message**,* as specified in \[10\] Page
            II-E-8 Section C-3

2.  ***Filing Service***

    1.  Input messages:

        1.  ***Filed Flight Plan Message**,* as specified in \[10\] Page
            II-E-10 Section C-4

        2.  ***Flight Plan Update Message**,* as specified in \[10\]
            Page II-E-19 Section C-9

        3.  ***Flight Cancellation Message<sup>8</sup>**,* as specified
            in \[10\] Page II-E-17 Section C-8

    2.  Output messages:

        1.  ***Submission Response Message**,* as specified in \[10\]
            Page II-C-1 Section C-1

        2.  ***Filing Status Message**,* as specified in \[10\] Page
            II-E-14 Section C-5

3.  ***Flight Data Request Service***

    1.  Input messages:

        1.  ***Flight Data Request Message**,* as specified in \[10\]
            Page II-E-24 Section C-10

    2.  Output messages:

        1.  ***Flight Data Response Message**,* as specified in \[10\]
            Page II-E-26 Section C-11

        2.  ***Submission Response Message**,* as specified in \[10\]
            Page II-C-1 Section C-1

Messages can be arranged according to the source that sends the message;
however, the initiative of the communication is another aspect to be
evaluated to select a suitable service implementation.

In all the input messages introduced above, the initiative of the
communication is taken by the service consumer; these messages are
called *requests*. Every time a service provider receives a *request*
message, they will send back an output message. Those output messages,
known as *reply* messages, are triggered by the reception of the
*request* message and therefore the initiative of such communication is
taken by the service consumer.[40]

In contrast, some output messages can be sent by the service provider on
its own initiative. These messages are called push messages or
*notification* messages.[41]

In order to document the FIXM-Based examples in this section, two sets
of technologies have been selected that accommodate the need to exchange
request, reply, and notification messages:

-   **SOAP Web Service technologies** allow to exchange request and
    reply messages where the initiative is taken by the service
    consumer.[42]

-   **AMQP** supports the exchange of notification messages where the
    initiative is taken by the service provider.

The following set of tables describes a possible design of FIXM-Based
Services in support of the FF-ICE/R1 Services described in \[10\].

<table>
<thead>
<tr class="header">
<th><em><strong>PlanningService</strong></em></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Technical Implementation</em></td>
<td><em>Operational</em></td>
<td></td>
</tr>
<tr class="even">
<td>Web Service Op.</td>
<td>Web Service Request/Reply</td>
<td>FF-ICE Message</td>
</tr>
<tr class="odd">
<td>submitPreliminaryFlightPlan</td>
<td>preliminaryFlightPlanSubmissionRequest</td>
<td><em><strong>Preliminary Flight Plan Message</strong></em></td>
</tr>
<tr class="even">
<td></td>
<td>preliminaryFlightPlanSubmissionReply</td>
<td><p><em><strong>Submission Response Message,</strong></em></p>
<p><em><strong>Planning Status Message</strong></em><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p></td>
</tr>
<tr class="odd">
<td>updatePreliminaryFlightPlan</td>
<td>preliminaryFlightPlanUpdateRequest</td>
<td><em><strong>Flight Plan Update Message</strong></em></td>
</tr>
<tr class="even">
<td></td>
<td>preliminaryFlightPlanUpdateReply</td>
<td><p><em><strong>Submission Response Message,</strong></em></p>
<p><em><strong>Planning Status Message<sup>12</sup></strong></em></p></td>
</tr>
<tr class="odd">
<td>cancelPreliminaryFlightPlan</td>
<td>preliminaryFlightPlanCancellationRequest</td>
<td><p><em><strong>Flight</strong></em></p>
<p><em><strong>Cancellation Message</strong></em></p></td>
</tr>
<tr class="even">
<td></td>
<td>preliminaryFlightPlanCancellationReply</td>
<td><p><em><strong>Submission Response Message,</strong></em></p>
<p><em><strong>Planning Status Message<sup>12</sup></strong></em></p></td>
</tr>
<tr class="odd">
<td></td>
<td>AMQP Notifications</td>
<td>FF-ICE Message</td>
</tr>
<tr class="even">
<td></td>
<td>FlightPlanningResultMessage</td>
<td><em><strong>Submission Response Message</strong></em> (<em><strong>ACK</strong></em> OR <em><strong>REJ</strong></em>)</td>
</tr>
<tr class="odd">
<td></td>
<td>PlanningStatusMessage</td>
<td><em><strong>Planning Status Message</strong></em></td>
</tr>
<tr class="even">
<td><em><strong>FilingService</strong></em></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><em>Technical Implementation</em></td>
<td><em>Operational</em></td>
<td></td>
</tr>
<tr class="even">
<td>Web Service Op.</td>
<td>Web Service Request/Reply</td>
<td>FF-ICE Message</td>
</tr>
<tr class="odd">
<td>submitFlightPlan</td>
<td>flightPlanSubmissionRequest</td>
<td><em><strong>Filed Flight Plan Message</strong></em></td>
</tr>
<tr class="even">
<td></td>
<td>flightPlanSubmissionReply</td>
<td><p><em><strong>Submission Response Message,</strong></em></p>
<p><em><strong>Filing Status Message</strong></em><a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></p></td>
</tr>
<tr class="odd">
<td>updateFlightPlan</td>
<td>flightPlanUpdateRequest</td>
<td><em><strong>Flight Plan Update Message</strong></em></td>
</tr>
<tr class="even">
<td></td>
<td>flightPlanUpdateReply</td>
<td><p><em><strong>Submission Response Message,</strong></em></p>
<p><em><strong>Filing Status Message<sup>13</sup></strong></em></p></td>
</tr>
<tr class="odd">
<td>cancelFlightPlan</td>
<td>flightPlanCancellationRequest</td>
<td><em><strong>Flight Cancellation Message</strong></em></td>
</tr>
<tr class="even">
<td></td>
<td>flightPlanCancellationReply</td>
<td><p><em><strong>Submission Response Message,</strong></em></p>
<p><em><strong>Filing Status Message<sup>13</sup></strong></em></p></td>
</tr>
<tr class="odd">
<td></td>
<td>AMQP Notifications</td>
<td>FF-ICE Message</td>
</tr>
<tr class="even">
<td></td>
<td>FlightFilingResultMessage</td>
<td><em><strong>Submission Response Message</strong></em> (<em><strong>ACK</strong></em> OR <em><strong>REJ</strong></em>)</td>
</tr>
<tr class="odd">
<td></td>
<td>FilingStatusMessage</td>
<td><em><strong>Filing Status Message</strong></em></td>
</tr>
</tbody>
</table>
<section class="footnotes" role="doc-endnotes">
<hr />
<ol>
<li id="fn1" role="doc-endnote"><p>The inclusion of the Planning Status Message in the reply is optional. See section 3.3.3 for more details.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2" role="doc-endnote"><p>The inclusion of the Filing Status Message in the reply is optional. See section 3.3.4 for more details.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

<table>
<thead>
<tr class="header">
<th><em><strong>FlightDataRequestService</strong></em></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Technical Implementation</em></td>
<td><em>Operational</em></td>
<td></td>
</tr>
<tr class="even">
<td>Web Service Op.</td>
<td>Web Service Request/Reply</td>
<td>FF-ICE Message</td>
</tr>
<tr class="odd">
<td>retrieveFlightPlanInformation</td>
<td>flightPlanRetrievalRequest</td>
<td><em><strong>Flight Data Request Message</strong></em></td>
</tr>
<tr class="even">
<td></td>
<td>flightPlanRetrievalReply</td>
<td><p><em><strong>Submission Response Message,</strong></em></p>
<p><em><strong>Flight Data Response Message</strong></em></p></td>
</tr>
</tbody>
</table>


There is some validation functionality that an XML schema alone cannot
provide. For example, there is no way for an XSD to make a particular
XML element required or optional based on the content of another
element. However, some message exchange business rules require exactly
these sorts of checks.

Schematron is a validation language capable of handling business rules
of this nature. As such, the use of Schematron can supplement the
limitations of XSDs and provide enforcement of any business rules
outside the scope of what XML schemas can offer.

**Error! Reference source not found.** provides examples of FIXM
business rules that could be encoded and checked using Schematron
technology. Schematron encodings are however not provided in this
version of the document. Future versions may revisit the overall
formulation and description method for FIXM business rules, in
particular in the light of the related AIXM experience.


Research Goal

What do you want to know, prove, demonstrate, analyze, test, investigate
or examine? List your project goals…for example…

•The goal of this research is to:

oIllustrate a new methodology/architecture/product/invention that has
never been built before

oDetermine the efficacy of your new
method/architecture/product/invention

oCreation of a research roadmap as it pertains to my new
method/architecture/product/invention

Background and/or Theories

What is already known or unknown? What past research are you building
upon?

Hypotheses (optional)

Depending on the nature of you research, hypothesis might not be stated
up front. For example, if you choose a qualitative research

method that leverages grounded theory, then a the “theory” is an
emergent property at the END of your research (i.e., a theory is

developed inductively not deductively when using grounded theory).
However, if your method is Quantitative or Design Science

oriented, then you should include verbiage upfront in your proposal that
discusses what your hypothesis (or hypotheses will be).

Methodology

Research Goal

What do you want to know, prove, demonstrate, analyze, test, investigate
or examine? List your project goals…for example…

•The goal of this research is to:

oIllustrate a new methodology/architecture/product/invention that has
never been built before

oDetermine the efficacy of your new
method/architecture/product/invention

oCreation of a research roadmap as it pertains to my new
method/architecture/product/invention

Background and/or Theories

What is already known or unknown? What past research are you building
upon?

Hypotheses (optional)

Depending on the nature of you research, hypothesis might not be stated
up front. For example, if you choose a qualitative research

method that leverages grounded theory, then a the “theory” is an
emergent property at the END of your research (i.e., a theory is

developed inductively not deductively when using grounded theory).
However, if your method is Quantitative or Design Science

oriented, then you should include verbiage upfront in your proposal that
discusses what your hypothesis (or hypotheses will be).

