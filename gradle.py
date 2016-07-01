from org.gradle.api.plugins import ApplicationPluginConvention

project.apply({'plugin': 'io.ratpack.ratpack-java'})
project.apply({'plugin': 'idea'})
project.repositories(lambda repos: repos.jcenter())
project.dependencies(lambda deps : deps.compile('org.python:jython-standalone:2.7.1b3'))
