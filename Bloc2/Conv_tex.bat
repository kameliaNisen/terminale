for %%f in (exo*.ipynb) do jupyter nbconvert --to pdf %%f
timeout 5