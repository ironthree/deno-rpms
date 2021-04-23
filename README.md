# Work-in-progress RPM packages for deno

This repository contains packaging-related files for the work-in-progress
RPM packages of deno and its dependencies.

Builds are available on COPR: <https://copr.fedorainfracloud.org/coprs/decathorpe/deno/>

## FIXMEs

- `ast_node`:
  - missing LICENSE files
  - bump darling from 0.10 to 0.12
- `async-stream`:
  - enable tests after updating tokio-test to ^0.4
- `console_error_panic_hook`:
  - missing LICENSE files
- `deno_console`:
  - missing LICENSE file
- `deno_core`:
  - missing LICENSE file
  - bundled ICU data?
- `deno_crypto`:
  - missing LICENSE file
- `deno_file`:
  - missing LICENSE file
- `deno_lint`:
  - bump deno_core from 0.84 to 0.85
  - shebang mangling of executable typescript files broken
- `deno_timers`:
  - missing LICENSE file
- `deno_url`:
  - missing LICENSE file
- `deno_web`:
  - missing LICENSE file
- `deno_webidl`:
  - missing LICENSE file
- `dprint-plugin-typescript`:
  - bump dprint-swc-ecma-ast-view from 0.15 to 0.16
- `dprint-swc-ecma-ast-view`:
  - missing LICENSE file
- `enum_kind`:
  - missing LICENSE files
- `from_variant`:
  - missing LICENSE files
- `gfx-backend-empty`:
  - missing LICENSE files
- `gfx-hal`:
  - missing LICENSE files
- `gpu-alloc`:
  - missing LICENSE files
- `gpu-alloc-types`:
  - missing LICENSE files
- `gpu-descriptor`:
  - missing LICENSE files
- `gpu-descriptor-types`:
  - missing LICENSE files
- `Inflector`:
  - missing LICENSE file
- `is-macro`:
  - missing LICENSE file
  - fix typos in description
- `naga`:
  - missing LICENSE files
- `pomelo-impl`:
  - missing LICENSE files
- `rustls`:
  - missing LICENSE files
  - two failing tests
- `rustls-native-certs`:
  - exclude upstream-only CI files
- `rusty_v8`:
  - missing LICENSE files
- `serde_v8`:
  - missing LICENSE file
- `sourcemap`:
  - bump rustc_version from 0.2.3 to 0.3
- `spirv_headers`:
  - missing LICENSE file
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
- `webpki`:
  - bump base64 from 0.9 to 0.13
- `wgpu-types`:
  - missing LICENSE file

## Dependency graph (TODO only)

- crates without version: not packaged as RPMs yet (neither Fedora nor COPR)
- crates with version: version in Fedora is either too old or too new
- crates that are packaged for Fedora or in this repo + COPR are not listed

```
deno
  | → deno_runtime
    | → deno_fetch
      | → reqwest/rustls-tls ^0.11.2
    | → deno_webgpu
      | → wgpu-core
        | → gfx-backend-gl
          | → gfx-auxil
          | → glow
          | → khronos-egl
          | → spirv_cross
        | → gfx-backend-vulkan
          | → ash
          | → inplace_it
    | → deno_websocket
      | → tokio-tungstenite/rustls-tls ^0.14
    | → notify ^5.0.0-pre.7
    | → ring ^0.16.20
    | → sys-info ^0.8.0
  | → lspower
    | → async-tungstenite
    | → auto_impl
    | → lspower-macros
    | → lsp-types
    | → tower-test ^0.4.0
    | → ws_stream_tungstenite
  | → notify ^5.0.0~pre.6
  | → ring ^0.16.20
  | → rustyline ^8.0.0
  | → rustyline_derive ^0.4.0
  | → swc_bundler
  | → tower-test ^0.4.0
  | → trust-dns-client
  | → trust-dns-server
```

## Pending package changes in Fedora

- enable Rustls features in `reqwest`
- enable Rustls features in `trust-dns-*`

## License

All published downstream code (.spec and .diff / .patch) is made available
under the terms of the default software license for Fedora packages according
to the Fedora Project Contributor Agreement / "FPCA" (the **MIT** license) [¹],
since all RPM packages maintained in this repository will eventually become
official Fedora packages.

[¹]: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement

