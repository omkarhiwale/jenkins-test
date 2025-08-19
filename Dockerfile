# Use Apache HTTP server official image
FROM httpd:2.4

# Copy custom index.html
COPY ./index.html /usr/local/apache2/htdocs/index.html

echo "<h1>Hello from Apache + Jenkins + Docker!</h1>" > index.html
