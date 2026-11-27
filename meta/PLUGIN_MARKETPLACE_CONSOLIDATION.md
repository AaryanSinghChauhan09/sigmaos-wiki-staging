# SigmaOS Plugin Marketplace Architecture Assessment

## Repository Overview

The SigmaOS plugin marketplace ecosystem consists of the following repositories:

### Core Repositories

1. **SigmaOS-plugin-marketplace**
   - Purpose: Component definition and contract specification
   - Status: Single COMPONENT.toml file defining marketplace contracts
   - Recommendation: Keep as component definition - minimal, no consolidation needed

2. **SigmaOS-plugin-registry**
   - Purpose: Rails control plane for plugin registry (plugins.sigmaos.org)
   - Status: Full Rails application with database, accounts, publishing
   - Technology: Ruby on Rails, Turso/libSQL, Better Auth
   - Recommendation: Keep as independent registry - core infrastructure

3. **SigmaOS-plugin-marketplace-tools**
   - Purpose: Consolidated repository containing:
     - `site/`: Static marketplace frontend
     - `worker/`: Cloudflare Worker engagement backend
     - `registry.json`: Curated registry data
     - `scripts/`: Build scripts, security baseline scanning, verification
   - Status: Active development, consolidated site + worker + tools
   - Recommendation: This is the correct consolidation - keeps frontend, backend, and tools together

4. **SigmaOS-plugin-marketplace-site**
   - Purpose: Modular split of the site directory
   - Status: README indicates this is a modular split
   - Recommendation: **ARCHIVE** - this repo is superseded by SigmaOS-plugin-marketplace-tools

5. **SigmaOS-plugin-marketplace-worker**
   - Purpose: Separate worker repository
   - Status: Likely superseded by worker/ in consolidated tools repo
   - Recommendation: **ARCHIVE** - this repo is superseded by SigmaOS-plugin-marketplace-tools

## Architecture Summary

### Current State (After Consolidation)

```
SigmaOS-plugin-marketplace (component definition)
    ↓
SigmaOS-plugin-registry (Rails control plane - plugins.sigmaos.org)
    ↓
SigmaOS-plugin-marketplace-tools (consolidated: site + worker + scripts + registry.json)
```

### Consolidation Actions Required

1. **Archive SigmaOS-plugin-marketplace-site**
   - Add README note pointing to SigmaOS-plugin-marketplace-tools
   - Mark as deprecated in GitHub repository topics
   - Reason: Site code now lives in SigmaOS-plugin-marketplace-tools/site/

2. **Archive SigmaOS-plugin-marketplace-worker**
   - Add README note pointing to SigmaOS-plugin-marketplace-tools
   - Mark as deprecated in GitHub repository topics
   - Reason: Worker code now lives in SigmaOS-plugin-marketplace-tools/worker/

3. **Keep SigmaOS-plugin-marketplace**
   - Maintains component contract definition
   - No changes needed

4. **Keep SigmaOS-plugin-registry**
   - Maintains Rails control plane infrastructure
   - No changes needed

5. **Keep SigmaOS-plugin-marketplace-tools**
   - This is the active development repository
   - Contains the full marketplace stack

## Rationale

The plugin marketplace requires three distinct concerns:

1. **Component Contract** (SigmaOS-plugin-marketplace)
   - Defines marketplace contracts between components
   - Minimal metadata only
   - Should remain separate

2. **Registry Infrastructure** (SigmaOS-plugin-registry)
   - Rails application with database
   - Accounts, publishing, review, admin
   - Requires separate infrastructure and deployment
   - Should remain independent

3. **Marketplace Frontend + Tools** (SigmaOS-plugin-marketplace-tools)
   - Static site (HTML/CSS/JS)
   - Cloudflare Worker for engagement metrics
   - Build scripts and security scanning
   - These work together and benefit from being in one repo
   - Already consolidated

## Benefits of This Architecture

- **Clear separation of concerns**: Component definition, registry infrastructure, and frontend/tools are separate
- **Appropriate coupling**: Frontend, worker, and build scripts are tightly coupled in one repo
- **Independent infrastructure**: Registry can be deployed separately from the static site
- **Minimal repo count**: 3 active repos instead of 5
- **Clearer development workflow**: All frontend/tool development happens in one place

## Migration Path

No code migration needed - the split repos (site, worker) are already superseded by the consolidated tools repo. Actions:

1. Archive the two split repos with deprecation notices
2. Update any external references to point to SigmaOS-plugin-marketplace-tools
3. Update documentation to reflect the 3-repo architecture

## Status

- ✅ Assessment complete
- ✅ Archived SigmaOS-plugin-marketplace-site on GitHub (2026-11-25)
- ✅ Archived SigmaOS-plugin-marketplace-worker on GitHub (2026-11-25)
- ✅ SigmaOS-plugin-marketplace: Keep as-is
- ✅ SigmaOS-plugin-registry: Keep as-is
- ✅ SigmaOS-plugin-marketplace-tools: Keep as-is (consolidated)

---

Assessment Date: 2026-10-15
