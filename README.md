# nothing-to-see-here
please stop looking at me.  Eventually this might do something.  For now, it just helps you waste about 10-15 min.

![Example graph](http://static.boredpanda.com/blog/wp-content/uuuploads/funny-graphs-2/funny-graphs-lady-gaga.jpg)

Placeholder for super secret stuff which is totally not public at all.

If using this, you might find yourself doing the following:

- Programing in Python 2.7
- Collecting a specific data set via API
- Using MySQL as a relational, on-disk database for retrieved data storage
- Using Flask and D3 to build visualizations

# Developing

If you found yourself here, you are in need of far more help than I can provide.  I recommend a life-coach.

To get started with developing on this repo:

- Clone the repository.
- Create a virtualenv for the repo. Run command `virtualenv .`
- Activate the virtualenv `. bin/activate`
- Install the requirements `pip install -r requirements.txt` in the virtualenv.
- Create schema in MySQL using `create schema lazercatzen;`
- Make a copy of `example-settings.json` and change the name to `settings.json` then add your MySQL user and password
- Run using command `python runner.py`

# Contributing

Submit a PR. Totally.   If you manage to make sense of what I'm doing and can contribute meaningfully, I totally welcome input.

Any PR requires at least one +1 from myself and another contributer.  Since I'm so far the only contributor, I find a catch-22 in the making.

- Create a branch off master.
- Make your changes until your new report or feature works.
- Test (if possible) that all other pre-existing features work. If this seems hard or mysterious, let us know and we can do it.
- Check that your Python reasonably meets pep8 standards: $ pep8 #your_file#
- If your code editor has an Inspect Code feature, inspect it and make any reasonable changes.
- Combine the code with the current master branch. While on your branch, type in: $ git merge master
- Submit a Pull Request, and drop it into the #implementation channel

When code is approved for merging, we'll plus one it, and it'll be up to you to merge the code and delete the branch. Let us know when it's done, and we can pick a time to deploy the code to the servers that will be least interruptive to currently running reports.

# Monitoring

All local via your own system currently