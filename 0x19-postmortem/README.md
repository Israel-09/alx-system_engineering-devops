# Postmortem: High User Complaints Due to Low ULIMIT

## Date: 14th October, 2023
## Author: Inene Israel

### Overview

On 14th October, 2023, our DevOps team was confronted with a critical challenge as we observed a sharp uptick in user complaints regarding sluggish server response times and subpar website performance. It was evident that our server infrastructure was strained, and the investigation revealed a pivotal issue – an improperly configured `ULIMIT` setting on the web server. This postmortem report delves into the root cause of the problem, the challenges encountered during resolution, the solutions implemented, and the crucial follow-up actions required.

### Problem Cause

**Root Cause**: The crux of our server performance issues lay in the `ULIMIT` setting on the web server.

**Details**:
- `ULIMIT`, a crucial parameter governing user process resource limits in Unix-based systems, had an inadequately low default setting on our web server.
- This left our server ill-equipped to handle the surging user load, leading to poor response times, degraded user experience, and, in severe cases, server crashes.

!(granny with many open tabs)[https://4.bp.blogspot.com/--v8xaxwow80/Vp1_z5QDC-I/AAAAAAACpoU/DNJ2WhquuCc/s640/IMG_2874.JPG]

### Challenges Faced

In dealing with this incident, we encountered a range of formidable challenges:

1. **User Impact**: The escalating user complaints were not only detrimental to our reputation but also necessitated immediate resolution to sustain customer satisfaction.

2. **Diagnostic Complexity**: Identifying the root cause of the problem was intricate due to the multifaceted nature of server performance issues, which could be attributed to various factors other than the `ULIMIT` setting.

3. **Downtime Risk**: Adjusting `ULIMIT` settings involves potential disruption of server operations, posing a risk of temporary service unavailability.

### Solution

To remediate the `ULIMIT` issue and restore optimal service quality, we meticulously executed the following measures:

1. **Immediate Mitigation**:
   - In an effort to address the immediate concern, we promptly raised the `ULIMIT` settings for the web server to a more suitable level.

2. **Configuration Analysis and Management**:
   - A thorough examination of server configurations was performed, with a particular focus on resource limits such as `ULIMIT`.
   - We introduced a configuration management system to define, track, and version server configurations, thereby ensuring a clear overview of settings and timely identification of deviations from best practices.

3. **Automated Remediation and Monitoring**:
   - Automation scripts and tools were developed to enact configuration adjustments based on predefined policies. This allowed for automatic `ULIMIT` setting adjustments in response to variations in server load or resource utilization.
   - The monitoring and alerting systems were augmented to proactively detect deviations in server configurations and to alert the team to any anomalies. This ensured timely responses to configuration-related issues.

4. **Testing and Deployment**:
   - Changes to `ULIMIT` settings were thoroughly evaluated in a testing environment to gauge their impact on server performance and stability.
   - Following successful testing, the new `ULIMIT` settings were deployed to the production environment during a scheduled maintenance window to minimize user impact.

5. **Documentation and Knowledge Sharing**:
   - We updated our documentation to include detailed information about server configurations, best practices, and the rationale behind specific settings.
   - An internal knowledge sharing initiative was launched to enhance the team's collective understanding of configuration management.

6. **Regular Configuration Reviews**:
   - Instituted a practice of regular configuration reviews to ensure our server settings align with evolving performance requirements.

### Follow-up Actions

To maintain a resilient and well-configured infrastructure, we have outlined a set of ongoing actions:

1. **Continual Configuration Reviews**:
   - Ongoing and regular reviews of server configurations will be conducted to ensure alignment with changing requirements.

2. **Automated Policy Enforcement**:
   - We are expanding our automation capabilities to automatically enforce configuration policies, reducing the potential for human error.

3. **Configuration Drift Detection**:
   - Implement tools to detect real-time configuration drift, enabling us to rectify any deviations from the established configuration baseline promptly.

4. **Staff Training**:
   - Our team members will receive training and workshops to enhance their proficiency in configuration management, ensuring a comprehensive understanding of configuration implications.

5. **Incident Response Planning**:
   - Detailed incident response plans, specifically for configuration-related incidents, will be developed to ensure effective and prompt resolution.

The low `ULIMIT` setting emerged as the key factor behind the performance issues that triggered a surge in user complaints. By increasing `ULIMIT` settings and implementing proactive configuration management strategies, we successfully resolved the issue, thereby enhancing server performance and reliability. We commit to maintaining comprehensive documentation, investing in training and automation, and ensuring that regular configuration reviews remain a cornerstone of our infrastructure management. This postmortem report serves as a crucial learning experience, underscoring the significance of configuration management and proactive monitoring in maintaining a resilient and dependable infrastructure.

## link
[word Documentation](https://docs.google.com/document/d/1pcMyLaFOnuZg4tvr7ABrBa0cE1DIPs1vke5XgPx8D70/edit?usp=sharing)
