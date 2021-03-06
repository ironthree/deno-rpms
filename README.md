# Work-in-progress RPM packages for deno

This repository contains packaging-related files for the work-in-progress
RPM packages of deno and its dependencies.

Builds are available on COPR: <https://copr.fedorainfracloud.org/coprs/decathorpe/deno/>

## FIXMEs

- `ash`:
  - Rust source files have executable bits
  - missing LICENSE file
- `ast_node`:
  - missing LICENSE files
  - bump darling from 0.10 to 0.12
- `deno`:
  - missing LICENSE file
- `deno_console`:
  - missing LICENSE file
- `deno_core`:
  - missing LICENSE file
  - bundled ICU data?
- `deno_crypto`:
  - missing LICENSE file
- `deno_fetch`:
  - missing LICENSE file
- `deno_file`:
  - missing LICENSE file
- `deno_lint`:
  - bump deno_core from 0.84 to 0.85
  - shebang mangling of executable typescript files broken
- `deno_runtime`:
  - missing LICENSE file
- `deno_timers`:
  - missing LICENSE file
- `deno_url`:
  - missing LICENSE file
- `deno_web`:
  - missing LICENSE file
- `deno_webgpu`:
  - missing LICENSE file
- `deno_webidl`:
  - missing LICENSE file
- `deno_websocket`:
  - missing LICENSE file
- `dlopen_derive`:
  - missing LICENSE file
- `dprint-plugin-typescript`:
  - bump dprint-swc-ecma-ast-view from 0.15 to 0.16
- `dprint-swc-ecma-ast-view`:
  - missing LICENSE file
- `enum_kind`:
  - missing LICENSE files
- `from_variant`:
  - missing LICENSE files
- `gfx-auxil`:
  - missing LICENSE files
- `gfx-backend-empty`:
  - missing LICENSE files
- `gfx-backend-gl`:
  - missing LICENSE files
- `gfx-backend-vulkan`:
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
- `is-macro`:
  - missing LICENSE file
  - fix typos in description
- `lspower-macros`:
  - missing LICENSE files
- `naga`:
  - missing LICENSE files
- `pomelo-impl`:
  - missing LICENSE files
- `rusty_v8`:
  - missing LICENSE files
- `sourcemap`:
  - bump rustc_version from 0.2.3 to 0.3
- `spirv_cross`:
  - bundled SPIRV-Cross
  - missing license files
- `spirv_headers`:
  - missing LICENSE file
- `string_enum`:
  - missing LICENSE files
- `swc_atoms`:
  - missing LICENSE files
- `swc_bundler`:
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
- `wgpu-core`:
  - missing LICENSE file
- `wgpu-types`:
  - missing LICENSE file

## License

All published downstream code (.spec and .diff / .patch) is made available
under the terms of the default software license for Fedora packages according
to the Fedora Project Contributor Agreement / "FPCA" (the **MIT** license) [??],
since all RPM packages maintained in this repository will eventually become
official Fedora packages.

[??]: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement

