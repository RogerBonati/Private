return {
  {
    "stevearc/conform.nvim",
      lazy = true,
    cmd = "ConformInfo",
    config = function()
      local conform = require("conform")
      conform.setup({
        format = {
          timeout_ms =  3000,
          async = false,
          quiet = false,
        },
        formatters_by_ft = {
          lua = { "stylua" },
        },
        formatters = {
          injected = { options = { ignore_errors = true } },
        },
      })
    end,
  },
}

