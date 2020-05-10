load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_dependency_manager",
    sha256 = "9d1c2b2c2d1698fb7693d354a7c09f999fd2fe8d7a8c8aa1ea593e2c0902c054",
    strip_prefix = "bazel-dependency-manager-ad9c621307dff1300303981dde0425795bd301e9",
    urls = ["https://github.com/Slowki/bazel-dependency-manager/archive/ad9c621307dff1300303981dde0425795bd301e9.tar.gz"],
)

load("@bazel_dependency_manager//:repo_rules.bzl", "fetch_dependencies")

fetch_dependencies(
    {
        # Miscellaneous Bazel dependencies
        "rules_cc": {
            "source": "github:bazelbuild/rules_cc#8c31dd406cf17611d7962bee4680cbc4360219ed",
            "sha256": "072ebe7abf772ac73f862626427ed4a09bb0d5227cf4896d98bc41afdebd387b",
        },
        "rules_python": {
            "source": "github:bazelbuild/rules_python#a0fbf98d4e3a232144df4d0d80b577c7a693b570",
            "sha256": "76a8fd4e7eca2a3590f816958faa0d83c9b2ce9c32634c5c375bcccf161d3bb5",
        },
        "io_bazel_rules_go": {
            "source": "github:bazelbuild/rules_go#28dd92b09c978ad09c74c18161a1da844235adfb",
            "sha256": "a72d2515097cab11732201a8d2a110973a89da5e1a59276e6ef94bf4a891101d",
        },
        "com_github_bazelbuild_buildtools": {
            "source": "github:bazelbuild/buildtools#3.0.0",
            "sha256": "a0e79f5876a1552ae8000882e4189941688f359a80b2bc1d7e3a51cab6257ba1",
        },
        "bazel_skylib": {
            "source": "github:bazelbuild/bazel-skylib#560d7b2359aecb066d81041cb532b82d7354561b",
            "sha256": "0cf18d7ba964b6a4ef4b21d471e3541cd22f7594512d172274d86647a87a2ffe",
        },
        "bazel_gazelle": {
            "source": "github:bazelbuild/bazel-gazelle#v0.20.0",
            "sha256": "1528eedddaa24d4878c93785703dce4f7bfbabd868713e6d1b3ae950e6ec887b",
        },
        # Protobuf - required by com_github_bazelbuild_buildtools
        "com_google_protobuf": {
            "source": "github:protocolbuffers/protobuf#d0bfd5221182da1a7cc280f3337b5e41a89539cf",
            "sha256": "2435b7fb83b8a608c24ca677907aa9a35e482a7f018e65ca69481b3c8c9f7caf",
        },
        # Tools
        "generate_compile_commands": {
            "source": "github:Slowki/bazel-compile-commands#634eeabf407da3a723d934babe6909218cb27a62",
            "sha256": "ceb869d32f4d2fc45cc6f7226e83f8649cfcdbd537300b3de6ce848d94fbb40f",
        },
    },
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains()

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")

gazelle_dependencies()

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

load("@rules_python//python:pip.bzl", "pip3_import")

pip3_import(
    name = "pip",
    requirements = "//third_party:requirements.txt",
)

load("@pip//:requirements.bzl", "pip_install")

pip_install()
