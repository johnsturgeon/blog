# johnsturgeon.me

This contains the Jekyll files for my personal blog.

It's published to cloudflare pages

To preview locally:

```bash
cd myblog
bundle exec jekyll serve
```

To deploy:

```bash
cd myblog
bundle exec jekyll build
git add .
git commit -m "Some message here"
git push
```

A cloudflare page worker will build the jekyll site and publish it.
