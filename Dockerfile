FROM ruby:2.7
WORKDIR /jekyll-site
RUN gem install github-pages
ENTRYPOINT jekyll serve --profile --livereload --incremental --strict-front-matter --host 0.0.0.0
