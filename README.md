# Work-in-progress RPM packages for deno

This repository contains packaging-related files for the work-in-progress
RPM packages of deno and its dependencies.

Builds are available on COPR: <https://copr.fedorainfracloud.org/coprs/decathorpe/deno/>

## Dependency graph (incomplete)

Packages that do not have a version listed with them are not packaged as RPMs
for Fedora yet, and those *with* a version are packaged, but have a version that
is too old in Fedora. Crates that are already packaged with acceptable versions
are not listed.

```
deno
  | → deno_core
    | → log ^0.4.14
      | → sval ^1.0.0-alpha.5
        | → sval_derive ^1.0.0-alpha.5
        | → value_bag
          | → sval_json
        | → wasm-bindgen-test
          | → console_error_panic_hook
          | → wasm-bindgen-futures
    | → rusty_v8
    | → serde_v8
      | → serde_v8
  | → deno_doc
    | → swc_common
    | → swc_ecmascript
  | → deno_lint
    | → dprint-swc-ecma-ast-view
    | → swc_atoms
    | → swc_common
  | → deno_runtime
    | → deno_console
    | → deno_core
    | → deno_crypto
    | → deno_fetch
    | → deno_file
    | → deno_url
    | → deno_web
    | → deno_webgpu
    | → deno_webidl
    | → deno_websocket
  | → dprint-plugin-json
    | → dprint-core
    | → jsonc-parser
  | → dprint-plugin-markdown
    | → dprint-core
  | → dprint-plugin-typescript
    | → dprint-core
    | → dprint-swc-ecma-ast-view
    | → swc_common
    | → swc_ecmascript
  | → exec
  | → fancy-regex
  | → jsonc-parser
  | → log ^0.4.14
  | → lspower
    | → lspower-macros
    | → lsp-types
  | → notify ^5.0.0~pre.6
  | → ring ^0.16.20
  | → rustyline ^8.0.0
  | → rustyline_derive ^0.4.0
  | → sourcemap
  | → swc_bundler
    | → swc_atoms
    | → swc_common
    | → swc_ecma_ast
    | → swc_ecma_codegen
    | → swc_ecma_parser
    | → swc_ecma_transforms
    | → swc_ecma_utils
    | → swc_ecma_visit
  | → swc_common
    | → swc_eq_ignore_macros
    | → swc_visit
  | → swc_ecmascript
    | → swc_ecma_ast
    | → swc_ecma_codegen
    | → swc_ecma_dep_graph
    | → swc_ecma_parser
    | → swc_ecma_transforms
    | → swc_ecma_utils
    | → swc_ecma_visit
  | → text-size
  | → tokio-rustls
    | → rustls
    | → webpki
    | → webpki-roots
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

