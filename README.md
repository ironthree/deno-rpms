# Work-in-progress RPM packages for deno

This repository contains packaging-related files for the work-in-progress
RPM packages of deno and its dependencies.

Builds are available on COPR: <https://copr.fedorainfracloud.org/coprs/decathorpe/deno/>

## FIXMEs

- `ast_node`:
  - missing LICENSE files
  - bump darling from 0.10 to 0.12
- `console_error_panic_hook`:
  - missing LICENSE files
- `deno_core`:
  - missing LICENSE file
  - bundled ICU data?
- `enum_kind`:
  - missing LICENSE files
- `from_variant`:
  - missing LICENSE files
- `Inflector`:
  - missing LICENSE file
- `is-macro`:
  - missing LICENSE file
  - fix typos in description
- `rusty_v8`:
  - missing LICENSE files
- `serde_v8`:
  - missing LICENSE file
- `sourcemap`:
  - bump rustc_version from 0.2.3 to 0.3
- `string_enum`:
  - missing LICENSE files
- `sval_json`:
  - missing LICENSE files
- `swc_atoms`:
  - missing LICENSE files
- `swc_common`:
  - missing LICENSE files
  - bump parking_lot from 0.7.1 to 0.11
- `swc_ecma_ast`:
  - missing LICENSE files
- `swc_ecmascript`:
  - missing LICENSE files
- `swc_ecma_codegen`:
  - missing LICENSE files
- `swc_ecma_codegen_macros`:
  - missing LICENSE files
- `swc_ecma_dep_graph`:
  - missing LICENSE files
- `swc_ecma_loader`:
  - missing LICENSE files
- `swc_ecma_parser`:
  - missing LICENSE files
- `swc_ecma_transforms`:
  - missing LICENSE files
- `swc_ecma_transforms_base`:
  - missing LICENSE files
- `swc_ecma_transforms_compat`:
  - missing LICENSE files
- `swc_ecma_transforms_macros`:
  - missing LICENSE files
- `swc_ecma_transforms_module`:
  - missing LICENSE files
- `swc_ecma_transforms_optimization`:
  - missing LICENSE files
- `swc_ecma_transforms_proposal`:
  - missing LICENSE files
- `swc_ecma_transforms_react`:
  - missing LICENSE files
- `swc_ecma_transforms_typescript`:
  - missing LICENSE files
- `swc_ecma_utils`:
  - missing LICENSE files
- `swc_ecma_visit`:
  - missing LICENSE files
- `swc_eq_ignore_macros`:
  - missing LICENSE files
- `swc_macros_common`:
  - missing LICENSE files
- `swc_visit`:
  - missing LICENSE files
- `swc_visit_macros`:
  - missing LICENSE files
- `value-bag`:
  - one failing memory layout test on aarch64

## Dependency graph (TODO only)

- crates without version: not packaged as RPMs yet (neither Fedora nor COPR)
- crates with version: version in Fedora is either too old or too new
- crates that are packaged for Fedora or in this repo + COPR are not listed

```
deno
  | → deno_doc
  | → deno_lint
    | → annotate-snippets
      | → yansi-term
    | → derive_more ^0.99.13
      | → convert_case
    | → dprint-swc-ecma-ast-view
      | → pretty_assertions ^0.7.1
  | → deno_runtime
    | → deno_console
    | → deno_core
    | → deno_crypto
    | → deno_fetch
    | → deno_file
    | → deno_timers
    | → deno_url
    | → deno_web
    | → deno_webgpu
    | → deno_webidl
    | → deno_websocket
    | → notify ^5.0.0-pre.7
    | → ring ^0.16.20
    | → sys-info ^0.8.0
    | → tokio-rustls
    | → webpki
    | → webpki-roots
  | → dprint-plugin-json
    | → dprint-core
    | → jsonc-parser
  | → dprint-plugin-markdown
    | → dprint-core
  | → dprint-plugin-typescript
    | → dprint-core
    | → dprint-swc-ecma-ast-view
  | → exec
  | → fancy-regex
  | → jsonc-parser
  | → lspower
    | → lspower-macros
    | → lsp-types
  | → notify ^5.0.0~pre.6
  | → ring ^0.16.20
  | → rustyline ^8.0.0
  | → rustyline_derive ^0.4.0
  | → swc_bundler
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

