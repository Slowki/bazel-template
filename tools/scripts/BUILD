load("@rules_python//python:defs.bzl", "py_binary")
load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "format",
    srcs = ["format.py"],
    data = ["@com_github_bazelbuild_buildtools//buildifier"],
    visibility = ["//visibility:public"],
    deps = [
        requirement("black"),
        requirement("isort"),
        "@rules_python//python/runfiles",
    ],
)
