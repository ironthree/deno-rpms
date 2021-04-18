# Work-in-progress RPM packages for deno

This repository contains packaging-related files for the work-in-progress
RPM packages of deno and its dependencies.

Builds are available on COPR: <https://copr.fedorainfracloud.org/coprs/decathorpe/deno/>

## 

## Dependency graph (incomplete)

Packages that do not have a version listed with them are not packaged as RPMs
for Fedora yet, and those *with* a version are packaged, but have a version that
is too old in Fedora. Crates that are already packaged with acceptable versions
are not listed.

```
deno
  | → deno_core
    | → log ^0.4.14
      | → sval ^1.0.0-alpha.1
    | → rusty_v8
      | → align-data
    | → serde_v8
  | → deno_doc
  | → deno_lint
  | → deno_runtime
  | → dprint-plugin-json
  | → dprint-plugin-markdown
  | → dprint-plugin-typescript
  | → exec
  | → fancy-regex
  | → jsonc-parser
  | → log ^0.4.14
  | → lspower
  | → notify ^5.0.0~pre.6
  | → ring ^0.16.20
  | → rustyline ^8.0.0
  | → rustyline_derive ^0.4.0
  | → sourcemap
  | → swc_bundler
  | → swc_common
  | → swc_ecmascript
  | → text-size
  | → tokio-rustls
  | → tower-test ^0.4.0
  | → trust-dns-client
  | → trust-dns-server
```

## License

All published downstream code (.spec and .diff / .patch) is made available
under the terms of the default software license for Fedora packages according
to the Fedora Project Contributor Agreement / "FPCA" (the **MIT** license) [¹],
since all RPM packages maintained in this repository will eventually become
official Fedora packages.

[¹]: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement

