# Repository Creation Plan

## Status

- **Total SigmaOS components (Wiki)**: 261
- **GitHub repos**: ~373 (298+ confirmed `SigmaOS-*`)
- **Pending creation**: 125 repos (Wiki pages ready, rate-limited)

GitHub enforces a secondary rate limit on repository creation
(~a few per hour). Bulk creation resumes when the window resets.

## Pending repos (125)

SigmaOS-airbyte
SigmaOS-airflow
SigmaOS-altair
SigmaOS-apache-spark
SigmaOS-blender
SigmaOS-bokeh
SigmaOS-bottles
SigmaOS-brave
SigmaOS-cline
SigmaOS-codexcli
SigmaOS-command-code
SigmaOS-creative-tools-complete
SigmaOS-crewai
SigmaOS-cryptomator
SigmaOS-databricks
SigmaOS-dbeaver
SigmaOS-dbt
SigmaOS-deepseek-coder
SigmaOS-deskland
SigmaOS-desktop-environment
SigmaOS-docker
SigmaOS-drawio
SigmaOS-duckdb
SigmaOS-elasticsearch
SigmaOS-element
SigmaOS-epic-games
SigmaOS-excalidraw
SigmaOS-excel
SigmaOS-fivetran
SigmaOS-free-file-sync
SigmaOS-gedit
SigmaOS-ggplot2
SigmaOS-gimp
SigmaOS-go
SigmaOS-gog
SigmaOS-grafana
SigmaOS-grafana-loki
SigmaOS-gui-frameworks
SigmaOS-gui-frameworks-complete
SigmaOS-gui-toolkit
SigmaOS-hadoop
SigmaOS-handbrake
SigmaOS-hermes-agent
SigmaOS-julia
SigmaOS-jupyter
SigmaOS-kate
SigmaOS-kde-connect
SigmaOS-keepass
SigmaOS-keepassxc
SigmaOS-knime
SigmaOS-kvm-more
SigmaOS-langchain
SigmaOS-libreoffice
SigmaOS-libreoffice-base
SigmaOS-libreoffice-calc
SigmaOS-libreoffice-draw
SigmaOS-libreoffice-impress
SigmaOS-libreoffice-math
SigmaOS-libreoffice-writer
SigmaOS-librewolf
SigmaOS-lightdash
SigmaOS-local-send
SigmaOS-lookerstudio
SigmaOS-mailspring
SigmaOS-matplotlib
SigmaOS-metabase
SigmaOS-mongodb
SigmaOS-mongodb-compass
SigmaOS-music-production-complete
SigmaOS-mysql
SigmaOS-neovim
SigmaOS-nifi
SigmaOS-notepadpp
SigmaOS-obs-studio
SigmaOS-omacalc
SigmaOS-omachee
SigmaOS-omacon
SigmaOS-omacut
SigmaOS-omadots
SigmaOS-omapager
SigmaOS-omarchs
SigmaOS-omareel
SigmaOS-omasnap
SigmaOS-omaterm
SigmaOS-omaview
SigmaOS-omawrite
SigmaOS-onlyoffice
SigmaOS-openboard
SigmaOS-openclaw
SigmaOS-pandas
SigmaOS-plotly
SigmaOS-podman
SigmaOS-polars
SigmaOS-postgresql
SigmaOS-posthog
SigmaOS-powerbi
SigmaOS-prometheus
SigmaOS-proton
SigmaOS-python
SigmaOS-pytorch
SigmaOS-raven
SigmaOS-reactos
SigmaOS-redis
SigmaOS-r-lang
SigmaOS-rustdesk
SigmaOS-sas
SigmaOS-scala
SigmaOS-scikit-learn
SigmaOS-seaborn
SigmaOS-skyvia
SigmaOS-snowflake
SigmaOS-sql
SigmaOS-state-archive
SigmaOS-statsmodels
SigmaOS-superset
SigmaOS-syncthing
SigmaOS-tableau
SigmaOS-tensorflow
SigmaOS-trial
SigmaOS-trial-windows
SigmaOS-trino
SigmaOS-warp
SigmaOS-waterfox
SigmaOS-web-developer-tools
SigmaOS-winboat
SigmaOS-wine
SigmaOS-zen

## Retry procedure

```sh
# From any shell with gh authenticated:
while read r; do
  gh repo create "AaryanSinghChauhan09/$r" --public && sleep 30
done < missing.txt
```

Create `missing.txt` by diffing wiki component dirs vs `gh repo list`.

## Notes

- All repos are public per project policy.
- Each repo gets: README, LICENSE (GPL-3.0), COMPONENT.toml, AGENTS.md,
  tools-sigmaos.sh v2, and a wiki page in sigmaos-wiki-staging.
- `SigmaOS-shell` was created and merged with pre-existing Rust
  bindings (sigmaquickshell) + new QML layer.
