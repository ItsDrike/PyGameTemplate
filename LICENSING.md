# Licensing

This file explicitly lists all of the licenses used in this project.

The license of this project and it's fulltext is present in the `LICENSE.md` file in the root directory of the project.
By default, all of the code in this repository is licensed under this license, however this file is here to explicitly
define the list of excepted files (or parts of files, such as a constant, variable, class, or other object) which are
licensed under a different license or have different autor who should be accredited.

The licenses mentioned in this file will usually include the [SPDX License identifier](https://spdx.org/licenses), which
will unambiguiusly define that license. This allows us to avoid having to include the full-text for these licenses.
However if the project uses a license that isn't listed in this index, the full-text will be included.

This file does not list the full-text for each included license, as long as that license is listed in SPDX index,
which 

This does not include the licenses of the dependencies of this project. Those can be easily found as they are explicitly
listed in the dependency manager configuration. They usually have unambiguous sources and so it should be easy enough to
find their licenses. All licenses of these projects have to be compatible with this project's license.

## Style of this document

Each section will include a readable name of the license and if possible an 
[SPDX License Identifier](https://spdx.org/licenses) unambiguously defining the license. SPDX definitions include the
full-text on their webpage, allowing us to avoid having to clutter this file with it. However if this project uses resources
under a license which isn't present in this index, the full-text will still need to be included.

The format of these sections will be as follows: `[READABLE LICENSE NAME] (SPDX:[SPDX IDENTIFIER NAME])` and will use
3rd level header to separate the individual sections. This allows quick and easy lookups by searching this file
with automated tools. If we don't have an SPDX identifier, the format should be: 
`[READABLE NAME] (SPDX Identifier isn't available)`.

The individual licensed files under a given license will be groupped under a this section header with that license name.
All of these files will be split into multiple categories, depending on the project author they belong to.

If the copyright header of the files is present in the license (or in other sensible location), it should be used to group
the individual files together. This would be formatted as follows:

```
Applies to:
  - Copyright (c) [Year] [Organization/Author's name]
    All rights reserved
      - [File path from project's root]: [Which part of this file this license applies to]
      - [Another file following the above pattern]
  - Copyright (c) [Year] [Another Organization/Another Author's name]
    All rights reserved
      - [Same format as in above example]
```

If the copyright header isn't publically liseted, we can use the author's name, followed by their email address.

```
Applies to:
  - Copyright (c) [Year the original file was created, present year if not known] author@domain.xyz
    All rights reserved
      - [Files (in same format as in previous example)]
```

Alternatively, if copyright doesn't apply to that content, but it should be listed anyway, the organization/author's
name or the project's name can be used directly. 

If there is no copyright, it usually implies a permissive public domain license, these generally don't need to be 
mentioned, however if attribution of the original source is desired, the organization/author's name or the project's
name can be used directly.

```
Applies to:
  - Created by [Author/Organization name]
    - [Files (in same format as in previous example)]
  - Originally present in [Project name]
    - [Files (in same format as in previous example)]
  - Submitted annonymously
    - [Files (in same format as in previous example)]
```

In case the license full-text needs to be included (there's no SPDX identifier)

Legally, this isn't necessary, but after all files are listed under their respective license in ther respective 
copyright/source group, there will be a section linking each mentioned copyright/source group with the original
author. This can be done via a link to author's page on github/gitlab/bitbucket or other similar service, or by
including their email. In case the source is annonymous, it can either be ommited. For example:
```
Applies to:
  - Copyright (c) 2020 John Doe
    All rights reserved
      - ./README.md: Installation section
  - Created by Tim Handerson
    - ./src/code.py: File inspired by the original creation
  - Copyright (c) 2014 Python Software Foundation (PSF)
    All rights reserved
      - ./.github/workflows/task.yml: lint workflow
  - Created by Michael Smith
    - ./.tox.ini: File inspired by the original creation
    - ./pyproject.toml: File inspired by the original creation
  - Submitted annonymously
    - ./src/regex.py: Phone number regex varaible.

Original source link(s):
  - John Doe:
    - <https://gitlab.com/JohnDoe>
  - Tim Handerson
    - <tim_handerson@example.com>
  - Python Software Foundation (PSD)
    - <https://github.com/python>
   - Michael Smith
    - <https://github.com/Michael_Smith/Some_Repository>
```


## License definitions

### MIT License (SPDX:MIT)

```
Applies to:
    - Copyright (c) 2018 Python Discord
      All rights reserved.
        - ./CONTRIBUTING.md: file was inspired by the original creation
        - ./.github/workflows/validation.yml: parts of lint job
        - ./src/util/log.py: file was inspired by the original creation

Original source link(s):
  - Python Discord:
    - <https://github.com/python-discord>
```
