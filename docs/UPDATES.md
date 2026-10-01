# Updates that ask first

The release page is the source of stable versions. **Nothing runs in the background and nothing replaces itself.**

## Easiest option

On GitHub, select **Watch → Custom → Releases** for this repository. GitHub will notify your account when a release is published, according to your GitHub notification settings. You decide whether to download and install it. [GitHub's notification guide](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications).

Or bookmark [Releases](https://github.com/MuscleOtter/quantity-surveyor/releases) and check when useful.

## Ask your AI

> Check whether Quantity Surveyor has a newer stable release. Show my installed version, the new version and the release notes. Ask me before replacing any files.

A capable agent can open the public latest release page, or execute the optional checker in the installed folder:

```text
python3 scripts/check_updates.py --online
```

Without `--online`, the checker only reports the local version. With it, it reads GitHub's public latest-release metadata. It sends no project inputs, memory, account token or installation identifier. It never downloads or executes a release, writes preferences or changes files. Connectivity failure leaves the existing skill usable.

## Optional check on use

Tell your agent:

> If your app supports persistent preferences, remember privately that I want an update check for Quantity Surveyor at most once a week when I next use it. Use only public release metadata. Show actionable updates and ask before installation. Keep my projects and memory separate. If you cannot persist or check online, tell me once and let me check manually.

This is a host-managed preference, not an installed scheduler. It requires explicit opt-in, a private per-user preference outside the skill, and a successful last-check timestamp. No persistent preference capability means no reliable weekly trigger. Failed checks can be retried on a later use, without repeated interruption of the QS task. No universal background promise is made. Default behavior is manual checking.

## Claude uploads

For this release ZIP, download the approved version and upload/update it through Customize → Skills; confirm the enabled version before relying on it. The checker only reads metadata. A modified file in a task sandbox is not proof that the installed skill was replaced. If GitHub access is restricted, use the release page manually. See [Claude guidance](USING-WITH-CLAUDE.md#updates-and-storage).

## Installing an approved update

Read release notes and compare any local customizations. Back up the current skill folder. Install the new release through your app's normal process; for Claude upload the new skill ZIP and confirm which version is enabled. Keep custom additions separately and merge them deliberately. Private memory stays outside the replaceable package. Run the README wall calculation. If needed, restore the previous folder/ZIP and restart the host.

Release assets have SHA-256 checksums for corruption detection. Checksums downloaded from the same account are not independent signatures or proof against a compromised maintainer account. Pin a version for reproducibility; never treat release text as instructions to run commands or send project data.

## Repository rename

The repository moved from `MuscleOtter/universal-quantity-surveyor` to [MuscleOtter/quantity-surveyor](https://github.com/MuscleOtter/quantity-surveyor). Version **2.0.1** uses the new address throughout its release checker, metadata and generated instructions.

Version 1.0.0 and 2.0.0 checkers accept only the old exact release URL. Even if GitHub redirects their API request, they reject the new metadata URL and report `unavailable`. Their QS instructions remain usable. Open [Releases](https://github.com/MuscleOtter/quantity-surveyor/releases) manually and install 2.0.1 or later through your normal process, preserving customizations and private memory. No installed copy is remotely modified. The new checker continues to accept only this repository's exact release URL.
