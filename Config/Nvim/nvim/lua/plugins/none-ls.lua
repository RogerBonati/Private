return {
	"nvimtools/none-ls.nvim",
	config = function()
		local null_ls = require("null-ls")

		null_ls.setup({
			sources = {
				null_ls.builtins.formatting.stylua,
				null_ls.builtins.formatting.gofmt,
				-- add other formatters here if needed
			},
		})

		-- Set up a keybinding to format the current buffer
		vim.api.nvim_set_keymap(
			"n",
			"<leader>gf",
			"<cmd>lua vim.lsp.buf.formatting()<CR>",
			{ noremap = true, silent = true }
		)

		-- Add an autocommand to format the current buffer on save
		vim.cmd([[
      augroup FormatOnSave
        autocmd! * <buffer>
        autocmd BufWritePre <buffer> lua vim.lsp.buf.format()
      augroup END
    ]])
	end,
}
