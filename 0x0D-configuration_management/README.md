## Configuration Management
> Learn how to use Puppet for managing configurations. Resources include
> [An Intro to Config Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management),
> [Puppet documentation](https://docs.puppet.com/puppet/3.5/type.html#file),
> [step by step Youtube video by Sylvain](https://www.youtube.com/watch?v=xmzbbe5bxrQ)

### Description of what each file shows:
Files that start with:
0. Create a file with specified path, permissions, owner, group, and text
1. Install puppet-lint 2.1.1 using puppet
2. Create a manifest that kills a process named killmenow

### How to use Puppet
```
$ gem install puppet-lint #install style checker
$ puppet-lint [filename]  #check style guide conform
$ puppet apply [filename] #set up your coded configurations
```

### Environment
* Language: puppet
* OS: Ubuntu 14.04 LTS
* Editor: [Emacs puppet mode](https://github.com/voxpupuli/puppet-mode)
* Style guidelines: [puppet-lint](http://puppet-lint.com/)
---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

