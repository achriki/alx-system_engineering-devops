# Postmortem Report

<p align="center">
<img src="https://raw.githubusercontent.com/MitaliSengupta/holberton-system_engineering-devops/master/0x19-postmortem/image.gif" width=100% height=100% />
</p>

## Issue Summary

- **Duration:** - March 5, 2024, 09:00 AM - March 6, 2024, 01:00 AM (UTC)
- **Impact:** - The user authentication service experienced a complete outage, affecting all users trying to log in. Approximately 80% of the total user base was unable to access the service during the outage.
- **Root Cause:** - A misconfiguration in the authentication service database replication setup led to a synchronization failure, causing the service to become unresponsive.

## Timeline

- **09:00 AM:** - Issue detected through monitoring alerts indicating high latency in user authentication requests.
- **09:10 AM:** - Engineering team notified of the issue.
- **09:20 AM:** - Investigation started, focusing on network connectivity and database performance.
- **10:30 AM:** - Misleading assumption made that the issue might be related to recent code deployments affecting database queries.
- **12:00 PM:** - Incident escalated to senior database administrator and system reliability engineering teams.
- **01:00 AM:** - Root cause identified as a misconfigured replication setup in the database cluster.
- **02:30 AM:** - Database configuration corrected, and service restored to full functionality.

## Root Cause and Resolution

- **Root Cause:** - The primary database server's replication settings were incorrectly configured, causing the standby server to fall out of sync, resulting in an inability to process authentication requests.
- **Resolution:** -  Database replication configuration was corrected, ensuring proper synchronization between the primary and standby servers. Additionally, monitoring and alerting were enhanced to promptly detect and notify of any synchronization failures in the future.

## Corrective and Preventative Measures

### Improvements/Fixes:

- Implement automated checks for database replication health and synchronization.
- Conduct regular audits of critical system configurations to catch misconfigurations early.
- Enhance documentation and training for the operations team regarding database replication setup and maintenance.

### Tasks to Address the Issue:

- Implement automated monitoring for database replication lag and failure.
- Conduct a comprehensive review of all critical system configurations to ensure correctness.
- Provide additional training sessions for operations team members on database replication management and troubleshooting.
