def week_entry(date, year, week, author):
    title = f"{year} Week {week}"
    return f"""---
title: {title}
author: {author}
date: {date}
---
# {title}

#{year}/weeks/{week}

## Week Goals

- [ ] Add your goal...
    """