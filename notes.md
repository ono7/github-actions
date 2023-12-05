## git hub action file structure

- events
  on: push (tracks events on the repo)

- jobs
  what happens after an event is captured

- runners

- steps

- actions

example:

```yaml
name: Surer linter

on: push # events

jobs: # jobs
  super-lint:
    name: "lints everything"
    runs-on: ubuntu-latest # this is the image to use
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Runs linter
        uses: github/surper-linter@v3
        env:
          DEFAULT_BRANCH: main
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
