[[leetcode discussion]](https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/)
  
# Requirements and Goals

- **Functional Requirements**
  - Given a URL, our service should generate a shorter and unique alias of it. 
  - - When users access a short link, our service should redirect them to the original link.
  - Users should optionally be able to pick a custom short link for their URL.
  - Links will expire after a standard default timespan. Users should be able to specify the expiration time. 
- **Non-Functional Requirements**
  - The system should be highly available. This is require because, if our service is down, all the URL redirectional will start failing.
  - URL redirection should happen in real-time with minimal latency.
  - Shortened links should not be guessable (not predictable).
- **Extended Requirements**
  - Analytics; how many times a redirection happened?
  - Our service should also be accessible through REST APIs by other services.

# Capacity Estimation and Constraints

# System APIs

# Database Design

# Basic System Design

# Data Partitioning and Replication

# Cache

# Load Balancer

# Purging or DB cleanup

# Telemetry

# Security and Permissions