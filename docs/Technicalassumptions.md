## Technical assumptions

The FF-ICE/R1 Implementation Guidance \[10\] mentions synchronous (e.g.
***Submission Response Message***) and asynchronous replies (e.g.
***Filing Status Message***) but does not provide definitions for these
terms. This complicates the interpretation of the FF-ICE/R1
interactions. For example does synchronous mean the client blocks until
the server replies or does it simply mean “timely”?

The chapter assumes the following:

1.  The request submission and the synchronous response are realized as
    SOAP request/reply.

2.  The asynchronous response is realized via an AMQP notification
    (which can be thought of as a message queue).

This is shown in the following diagram.

<img src=".//media/image247.png" style="width:4.07292in;height:1.5625in" />

<span id="_Ref508186374" class="anchor"></span>Figure 11: Synchronous
and asynchronous communication between eAU and eASP

In all the following examples, the diagrams will use the colour scheme
introduced by Figure 11: orange for synchronous communication, purple
for asynchronous.

### Setting up for asynchronous notifications

In order to setup the AMQP endpoint from which to receive the
asynchronous notifications the eAU needs to express such an interest to
the eASP.

The initiative to establish a connection could be on either side (client
or server). For example, the eAU could provide its own AMQP end-point to
which the eASP shall connect to publish the asynchronous notifications.
Conversely, an AMQP end-point could be created on the server side and
the client could connect to it to fetch the notifications. The latter
has the clear advantage of leveraging the server (i.e. the eASP) from
having to deal with all security-related issues (such as VPNs, firewall
rules, authentication, etc) for each eASP.

In the examples provided below, the eAU can invoke a specific web
service operation createSubscription by which it requests the eASP to
create an AMQP end-point on the server side to which it can then connect
to fetch the asynchronous notifications.

This is shown in the following diagram:

<img src=".//media/image248.png" style="width:5.07292in;height:1.47431in" />

<span id="_Toc48644023" class="anchor"></span>Figure 12:
SubscriptionCreationRequest to setup the AMQP end-point

The content of the SubscriptionCreationRequest should contain enough
information to allow the eASP to decide which notifications shall be
sent on this AMQP end-point (i.e. for which flights). Typically, the
subscription should at least cover all the flights filed or operated by
the eAU.

For example the content of such a request could be:

1.  Create a subscription for all flight plans operated by *\[operator
    name/id\]*

2.  Create a subscription for all flight plans submitted by *\[eAU
    name/id\]*

3.  Create a subscription for all flight plans flown by the following
    aircrafts *\[aircraft id\]*

4.  Create a subscription for all flight plans departing/arriving
    from/to the given airports *\[aerodrome id\]*

5.  Create a subscription for all flight plans that concern a given
    control centre *\[control centre id\]*

The content of the SubscriptionCreationReply contains the URL of the
AMQP end-point to which the eAU can connect.

This operation is to be invoked only once. Note that this AMQP channel
could also be created manually by the eASP following an agreement
between the eAU and the eASP.

All the examples in this chapter foresee the existence of this AMQP
channel. There will be four types of asynchronous messages:

1.  the FlightPlanningResultMessage,

2.  the PlanningStatusMessage,

3.  the FlightFilingResultMessage

4.  the FilingStatusMessage,

These messages are further explained in the following chapters.

<table>
<thead>
<tr class="header">
<th>Services Design Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em><strong>PlanningService</strong></em></p>
<p>SOAP Web Service Operations</p>
<blockquote>
<p>submitPreliminaryFlightPlan (preliminaryFlightPlanSubmissionRequest): preliminaryFlightPlanSubmissionReply</p>
<p>updatePreliminaryFlightPlan (preliminaryFlightPlanUpdateRequest): preliminaryFlightPlanUpdateReply</p>
<p>cancelPreliminaryFlightPlan (preliminaryFlightPlanCancellationRequest): preliminaryFlightPlanCancellationReply</p>
</blockquote>
<p>AMQP Notifications</p>
<blockquote>
<p>FlightPlanningResultMessage</p>
<p>PlanningStatusMessage</p>
</blockquote>
<p><em><strong>FilingService</strong></em></p>
<p>SOAP Web Service Operations</p>
<blockquote>
<p>submitFlightPlan (flightPlanSubmissionRequest): flightPlanSubmissionReply</p>
<p>updateFlightPlan (flightPlanUpdateRequest): flightPlanUpdateReply</p>
<p>cancelFlightPlan (flightPlanCancellationRequest): flightPlanCancellationReply</p>
</blockquote>
<p>AMQP Notifications</p>
<blockquote>
<p>FlightFilingResultMessage</p>
<p>FilingStatusgMessage</p>
</blockquote>
<p><em><strong>FlightInformationService</strong></em></p>
<p>SOAP Web Service Operations</p>
<blockquote>
<p>retrieveFlightPlanInformation (flightPlanRetrievalRequest): flightPlanRetrievalReply</p>
</blockquote></td>
</tr>
</tbody>
</table>

