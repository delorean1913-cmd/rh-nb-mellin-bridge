# Browser-only GitHub upload instructions

1. Download this zip file.
2. Unzip it.
3. Go to GitHub and create a new public repository named:

```text
rh-nb-mellin-bridge
```

4. Leave GitHub's README, `.gitignore`, and license boxes unchecked because these files are already included.
5. Open the unzipped folder on your computer.
6. Drag the **contents** of the folder into GitHub's upload page.
7. Use this commit message:

```text
Initial public NB/BD Mellin bridge package
```

8. Click **Commit changes**.
9. After the files are visible, copy the repository URL and paste it into `QUESTION.md`.
10. Create a release with:

```text
Tag: v0.1-public-question
Title: v0.1 public Mellin bridge question
```

Release notes:

```text
Initial public version of the NB/BD Mellin-side bridge question.

This release separates:
1. finite theorem artifacts / finite diagnostics,
2. the conjectural L2_eff bridge,
3. conditional RH implication through BD/NB.

No proof of RH is claimed.
```
