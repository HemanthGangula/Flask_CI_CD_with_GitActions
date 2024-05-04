# Flask_CI_CD_with_GitActions
🚀 Automate Flask web app CI/CD with GitHub Actions! Streamline testing &amp; deployment. Dive into seamless development workflows. Let's code &amp; deploy faster! 🌐💻 #Flask #GitHubActions #CI #CD

## Running the Pipeline
**Step 1:** Fork the Repository
- Fork the repository to your own GitHub account.

**Step 2:** Configure Docker Hub Credentials
- After forking the repository, configure Docker Hub credentials in the secrets of your forked repository.
- `Note: Instead of a password, use the Access Token in DcokerHub.`
- Create a Docker repository and add its details in the ci.yml file in place of my repository.
Once these two steps are completed, the CI pipeline is ready to be tested.

**Continuous Deployment:** 

**Step 3:** Set Up Self-Hosted Runner on AWS EC2
- Launch an EC2 instance.
- Ensure that port 5000 is added to the inbound rule for accessing the application.
- Connect to the instance via SSH:
- Run the following commands to update the packages 

```bash
sudo apt update
```
```bash
sudo apt upgrade
```
- In the forked repository in the github, go to Settings > Actions > Runners > New self-hosted runner.
- Follow the download and configure instructions to set up the self-hosted runner.
- Once configured, the self-hosted runner is ready for use.
**Testing the CD Pipeline**
- Access the application in your browser using <EC2_Public_IP>:5000.
- Any changes pushed to the repository will update the application within 30 seconds.
This setup ensures continuous integration and deployment of your application using GitHub Actions and AWS EC2.


