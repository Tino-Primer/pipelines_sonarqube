FROM sonarqube:8.9.8-community
COPY sonar.properties /opt/sonarqube/conf
EXPOSE 9090