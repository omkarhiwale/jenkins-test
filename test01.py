# Update system
sudo apt update -y

# Install Java if not installed
sudo apt install -y openjdk-17-jdk

# Download Tomcat 9 (latest)
cd /tmp
wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.98/bin/apache-tomcat-9.0.98.tar.gz

# Extract to /opt
sudo tar xzf apache-tomcat-9.0.98.tar.gz -C /opt/
sudo mv /opt/apache-tomcat-9.0.98 /opt/tomcat9

# Permissions
sudo chmod +x /opt/tomcat9/bin/*.sh

# Start Tomcat
/opt/tomcat9/bin/startup.sh
