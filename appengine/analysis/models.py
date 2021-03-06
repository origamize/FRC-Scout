#App Engine Models

from google.appengine.api import users
from google.appengine.ext import ndb
import string
import random
import sys
from datetime import datetime



'''
class Person(ndb.Model):
  """Models a person in the RPI directory."""
  first_name = ndb.StringProperty(indexed=False)
  prefered_name = ndb.StringProperty(indexed=False)
  middle_name = ndb.StringProperty(indexed=False)
  last_name = ndb.StringProperty(indexed=False)
  department = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)
  rcsid = ndb.StringProperty()
  year = ndb.StringProperty(indexed=False)
  major = ndb.StringProperty(indexed=False)
  title = ndb.StringProperty(indexed=False)
  phone = ndb.StringProperty(indexed=False)
  fax = ndb.StringProperty(indexed=False)
  homepage = ndb.StringProperty(indexed=False)
  office_location = ndb.StringProperty(indexed=False)
  campus_mailstop = ndb.StringProperty(indexed=False)
  mailing_address = ndb.StringProperty(indexed=False)
  date_crawled = ndb.DateTimeProperty(auto_now=True,indexed=False)
  directory_id = ndb.StringProperty(indexed=False)
  picture = ndb.BlobProperty()
  linked_account = ndb.UserProperty()
  has_picture = ndb.ComputedProperty(lambda self: True if self.picture else False)
  @property
  def has_pic(self): return 'true' if self.picture else 'false'
  @property
  def name(self): return generateName([self.first_name, self.middle_name, self.last_name])
  @property
  def mailing_address_html(self): return self.mailing_address.replace('\n', '<br />') if self.mailing_address else None
  @property
  def email_html(self): return self.email.replace('@', ' [at] ').replace('.', ' [dot] ') if self.email else None
  @property
  def type(self): return 'student' if self.major else ('faculty' if self.department else 'other')


  def update(self, d):
    for attr in person_attributes:
      v = d.get(attr,None)
      if v:
        if type(v) == type('string'):
          v = v.lower()
        setattr(self,attr,v)
  
  @staticmethod
  def buildPerson(d):
    if 'rcsid' not in d:
      return None
    person = Person(id = d['rcsid'])
    for attr in person_attributes:
      v = d.get(attr,None)
      if v:
        if type(v) == type('string'):
          v = v.lower()
        setattr(person,attr,v)
    return person
  
  @staticmethod
  def buildMap(p):
    d = {}
    for attr in map_attributes:
      v = getattr(p,attr,None)
      if v:
        if type(v) == type('string'):
          v = v.lower()
        d[attr] = v
    return d
  

class SearchPosition(ndb.Model):
  """Model to store Crawler position."""
  position = ndb.IntegerProperty()
      
class StatsObject(ndb.Model):
  """Model to hold statistics objects."""
  name = ndb.StringProperty(indexed=False)
  json = ndb.JsonProperty(indexed=False)
    
class SuggestObject(ndb.Model):
"""Model to hold suggestion objects."""
  name = ndb.StringProperty(indexed=False)
  json = ndb.JsonProperty(indexed=False)
'''
