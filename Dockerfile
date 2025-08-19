# Use Apache HTTP server official image
FROM httpd:2.4

# Copy custom index.html
COPY ./index.html /usr/local/apache2/htdocs/index.html

# Example: create index.html from inside Docker build
RUN echo "<h1>Hello from Jenkins + Docker + Apache!</h1>" > /usr/local/apache2/htdocs/index.html
