import xml.etree.ElementTree as ET
import struct
import logging

class XMLReader():
	@staticmethod
	def get_root(file_path):
		root = None
		try:
			tree = ET.parse(file_path)
			root = tree.getroot()
		except IOError as e:
			logging.info("File " + file_path + " can't be read.")
			logging.warning(e)
			raise(e)
		except Exception as e:
			logging.info("Unknown error on XML read.")
			logging.warning(e)
			raise e
		finally:
			return root
		

class LasStructure():
	"""docstring for LasStructure"""
	def __init__(self, las_structure_file_path, struct_settings_file_path):
		self.settings = None
		self.header = None
		self.blocks = None
		self.las_structure_file_path = las_structure_file_path
		self.struct_settings_file_path = struct_settings_file_path

	def create_las_file_structure(self):
		logging.debug('Creating las file structure')
		root = XMLReader.get_root(self.las_structure_file_path)
		for element in root.iter('settings'):
			settings = LasSettings()
			settings.build(element)

		for element in root.iter('header'):
			HeaderStructure(element)
			

class LasSettings():
	def __init__(self):
		self.variables = list()		

	def build(self, settings_element):
		for element in settings_element:
			key = ''.join(list(element.attrib.keys()))
			value = element.text
			self.variables.append({key: value})

class BaseStructure():
	"""docstring for HeaderStructure"""
	def __init__(self):
		self.variation_count = 0
		self.variation_list = list()

	def build(self, root):
		pass
		
class HeaderStructure(BaseStructure):
	"""docstring for HeaderStructure"""
	def __init__(self, arg):
		super(HeaderStructure, self).__init__()
		
	def build(self, root):
		pass

class BlockStructure(BaseStructure):
	"""docstring for BlockStructure"""
	def __init__(self, arg):
		super(BlockStructure, self).__init__()

	def build(self, root):
		pass		
		
		
		


logging.basicConfig(filename='las_reader.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')

if __name__ == '__main__':
	logging.info('Application starting.')
	las = LasStructure('las_structure_v2.xml', 'struct_settings.xml')
	las.create_las_file_structure()
	logging.info('Application exit.')

			


