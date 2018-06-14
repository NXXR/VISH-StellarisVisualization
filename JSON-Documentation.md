JSON Documentation
==================
Documentation of the JSON structure for further use.

Each element contains the status of the galaxy at the beginning of the year.

- `date`                *Date of the status*
- `system`              *Sublist of systems*
  - `index`               *Index of the system*
    - `coordinate`          *Sublist of coordinates*
      - `x`                   *x-coordinate*
      - `y`                   *y-coordinate*
    - `name`                *System name*
    - `planets`             *Array of planet indices*
    - `hyperlanes`          *Array of destinations (system indices)*
    - `starbase`            *Starbase index or null if no starbase present*
    - `fleet_presence`      *Array of fleet indices present in system*
    - `bypasses`            *Array of bypass indices present in system*
- `starbase`            *Sublist of starbases*
  - `index`               *Index of the starbase*
    - `level`               *Starbase Level (Outpost | Starport | Starhold | Starfortress | Citadel)*
    - `system`              *Location of the starbase (system index)*
    - `owner`               *Owner of the starbase (Country index)*
- `planet`              *Sublist of planets*
  - `index`               *Index of planet*
    - `name`                *Planet name*
    - `size`                *Planet size*
    - `tile_count`          *Planet tile count*
    - `last_bombardment`    *Last date the planet was under bombardment or null if N/A*
    - `owner`               *Owner of the planet (Country index)*
    - `surveyor`            *Surveyor of the planet (Country index)*
    - `pop_count`           *Number of Pops on planet*
    - `army_count`          *Number of Armies on planet*
    - `colonization_date`   *Date of planet colonization*