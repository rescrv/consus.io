title:  About Consus
url:
save_as:index.html
navbar: about

What is Consus?
===============

Consus is a **geo-replicated transactional key-value store** that upholds strong
consistency and fault tolerance guarantees across multiple data centers.  By
geo-replicating data, Consus can can withstand correlated failures up to and
including entire data centers, and reduce latency for clients by directing them
to nearby replicas.

The latency between geographically distinct locations forces storage systems to
navigate the inherent tradeoff between latency and fault tolerance.  Systems may
make an operation withstand a complete data center failure by incurring the
latency cost to propagate it to other data centers before reporting that the
operation has finished.  On the other side of the tradeoff systems, may avoid
the latency cost by reporting that an operation is complete before it propagates
to other data centers---at the risk that the operation is lost in a failure and
never takes effect in other data centers.  In essence, the tradeoff is entirely
a matter of minimizing latency while upholding desirable degree of fault
tolerance.  Consus chooses to **maintain fault tolerance at all times**.

What makes Consus unique?
=========================

For systems that make cross-data center fault tolerance guarantees, wide-area
latency is often the dominating cost.  An operation's overall execution time is
heavily dependent upon the number of messages sent via the wide area and the
latency of each message;  consequently, reducing the number of messages on the
critical path is an important aspect of optimizing the overall performance of
geo-replicated systems.

Consus can **commit a transaction across multiple data centers in three
wide-area message delays** during regular execution.  Simply sending a message
to a remote data center and receiving acknowledgement of its receipt---the bare
minimum necessary to tolerate a data center failure---requires two message
delays.  Protocols such as 2-phase commit or Paxos require two round trips, or
four message delays.

Who is behind Consus?
=====================

Consus is under active development in the Department of Computer Science at
Cornell University.  It is developed by [Robert Escriva](http://rescrv.net)
under the advisement of [Robbert van Renesse](https://www.cs.cornell.edu/home/rvr/).

How can I get Consus?
=====================

Consus is not currently available.

We are currently actively developing Consus and an associated tech report
describing its inner workings.  We will be publishing the source code concurrent
with the tech report under an open-source license.
