#Se importan los paquetes que seran utilizados
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterFeatureSink
import processing

# Se define al Model3
class Model3(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSink('Drop_fields_3', 'drop_fields_3', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Fixgeo_3', 'fixgeo_3', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Landq', 'landq', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Pop1800', 'pop1800', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Pop1900', 'pop1900', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Pop2000', 'pop2000', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(8, model_feedback)
        results = {}
        outputs = {}
        
        #######################################################################
        # Fix geometries
        #######################################################################
        #Se arregla la geometria del shp
        #######################################################################
        
        alg_params = {
            'INPUT': '/Users/gonzalorigirozzi/Downloads/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp',
            'OUTPUT': parameters['Fixgeo_3']
        }
        outputs['FixGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Fixgeo_3'] = outputs['FixGeometries']['OUTPUT']

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}
        
      
        #######################################################################
        # Zonal statistics
        #######################################################################
        # Se agrega campo que contiene la media de pop1900
        #######################################################################
        
        alg_params = {
            'COLUMN_PREFIX': 'pop1900',
            'INPUT': 'Zonal_Statistics_2a6c4e37_359e_4b84_9a83_cb416ce218f1',
            'INPUT_RASTER': 'popd_1900AD_38f5b80c_75c1_4819_8ec6_86e698d2f756',
            'RASTER_BAND': 1,
            'STATISTICS': [2],  # Mean
            'OUTPUT': parameters['Pop1900']
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Pop1900'] = outputs['ZonalStatistics']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}
        
        #######################################################################
        # Zonal statistics
        #######################################################################
        # Se agrega campo que contiene la media de pop1800
        #######################################################################
        
        alg_params = {
            'COLUMN_PREFIX': 'pop1800',
            'INPUT': 'Zonal_Statistics_d2796d7c_3e25_41f7_98ad_6238a3ec38ab',
            'INPUT_RASTER': 'popd_1800AD_e84b4e5a_3fa5_488f_824c_a4a1207346bb',
            'RASTER_BAND': 1,
            'STATISTICS': [2],  # Mean
            'OUTPUT': parameters['Pop1800']
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Pop1800'] = outputs['ZonalStatistics']['OUTPUT']

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}
        
        #######################################################################
        # Drop field(s)
        #######################################################################
        #Se eliminan campos que no seran utilizados.
        #######################################################################
        
        alg_params = {
            'COLUMN': ['featurecla','scalerank','LABELRANK','SOVEREIGNT','SOV_A3','ADM0_DIF','LEVEL','TYPE','TLC','ADM0_A3','GEOU_DIF','GEOUNIT','GU_A3','SU_DIF','SUBUNIT','SU_A3','BRK_DIFF','NAME','NAME_LONG','BRK_A3','BRK_NAME','BRK_GROUP','ABBREV','POSTAL','FORMAL_EN','FORMAL_FR','NAME_CIAWF','NOTE_ADM0','NOTE_BRK','NAME_SORT','NAME_ALT','MAPCOLOR7','MAPCOLOR8','MAPCOLOR9','MAPCOLOR13','POP_EST','POP_RANK','POP_YEAR','GDP_MD','GDP_YEAR','ECONOMY','INCOME_GRP','FIPS_10','ISO_A2','ISO_A2_EH','ISO_A3_EH','ISO_N3','ISO_N3_EH','UN_A3','WB_A2','WB_A3','WOE_ID','WOE_ID_EH','WOE_NOTE','ADM0_ISO','ADM0_DIFF','ADM0_TLC','ADM0_A3_US','ADM0_A3_FR','ADM0_A3_RU','ADM0_A3_ES','ADM0_A3_CN','ADM0_A3_TW','ADM0_A3_IN','ADM0_A3_NP','ADM0_A3_PK','ADM0_A3_DE','ADM0_A3_GB','ADM0_A3_BR','ADM0_A3_IL','ADM0_A3_PS','ADM0_A3_SA','ADM0_A3_EG','ADM0_A3_MA','ADM0_A3_PT','ADM0_A3_AR','ADM0_A3_JP','ADM0_A3_KO','ADM0_A3_VN','ADM0_A3_TR','ADM0_A3_ID','ADM0_A3_PL','ADM0_A3_GR','ADM0_A3_IT','ADM0_A3_NL','ADM0_A3_SE','ADM0_A3_BD','ADM0_A3_UA','ADM0_A3_UN','ADM0_A3_WB','CONTINENT','REGION_UN','SUBREGION','REGION_WB','NAME_LEN','LONG_LEN','ABBREV_LEN','TINY','HOMEPART','MIN_ZOOM','MIN_LABEL','MAX_LABEL','LABEL_X','LABEL_Y','NE_ID','WIKIDATAID','NAME_AR','NAME_BN','NAME_DE','NAME_EN','NAME_ES','NAME_FA','NAME_FR','NAME_EL','NAME_HE','NAME_HI','NAME_HU','NAME_ID','NAME_IT','NAME_JA','NAME_KO','NAME_NL','NAME_PL','NAME_PT','NAME_RU','NAME_SV','NAME_TR','NAME_UK','NAME_UR','NAME_VI','NAME_ZH','NAME_ZHT','FCLASS_ISO','TLC_DIFF','FCLASS_TLC','FCLASS_US','FCLASS_FR','FCLASS_RU','FCLASS_ES','FCLASS_CN','FCLASS_TW','FCLASS_IN','FCLASS_NP','FCLASS_PK','FCLASS_DE','FCLASS_GB','FCLASS_BR','FCLASS_IL','FCLASS_PS','FCLASS_SA','FCLASS_EG','FCLASS_MA','FCLASS_PT','FCLASS_AR','FCLASS_JP','FCLASS_KO','FCLASS_VN','FCLASS_TR','FCLASS_ID','FCLASS_PL','FCLASS_GR','FCLASS_IT','FCLASS_NL','FCLASS_SE','FCLASS_BD','FCLASS_UA'],
            'INPUT': 'Fixed_geometries_4984227e_126a_4f75_a4b2_9e6666294b4e',
            'OUTPUT': parameters['Drop_fields_3']
        }
        outputs['DropFields'] = processing.run('native:deletecolumn', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Drop_fields_3'] = outputs['DropFields']['OUTPUT']

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}
        
        #######################################################################
        # Zonal statistics
        #######################################################################
        # Se crea campo que contiene la media de Landq
        #######################################################################
        
        alg_params = {
            'COLUMN_PREFIX': '_',
            'INPUT': 'Remaining_fields_279a9ccd_b581_435c_a1b0_a9d24a4dcc2d',
            'INPUT_RASTER': 'landquality_ad42e93b_ac1b_48f0_9098_8e5f49043e3f',
            'RASTER_BAND': 1,
            'STATISTICS': [2],  # Mean
            'OUTPUT': parameters['Landq']
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Landq'] = outputs['ZonalStatistics']['OUTPUT']

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}
        
        #######################################################################
        # Zonal statistics
        #######################################################################
        # Se crea campo que contiene la media de pop2000
        #######################################################################
        
        alg_params = {
            'COLUMN_PREFIX': 'pop2000',
            'INPUT': 'Zonal_Statistics_e905fe3e_0b6a_4079_bafe_0df449f9a606',
            'INPUT_RASTER': 'popd_2000AD_8fd416b1_767c_4119_99c9_cf5d89d2e196',
            'RASTER_BAND': 1,
            'STATISTICS': [2],  # Mean
            'OUTPUT': parameters['Pop2000']
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Pop2000'] = outputs['ZonalStatistics']['OUTPUT']

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}
        
        #######################################################################
        # Save vector features to file
        #######################################################################
        # Se guarda en formato.gpkg
        #######################################################################
        
        alg_params = {
            'DATASOURCE_OPTIONS': '',
            'INPUT': 'Zonal_Statistics_90961545_cd97_4a17_8e85_1c091f1ffbc6',
            'LAYER_NAME': '',
            'LAYER_OPTIONS': '',
            'OUTPUT': '/Users/gonzalorigirozzi/Desktop/Clase 4/OUTPUT/raster_stats.gpkg',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['SaveVectorFeaturesToFile'] = processing.run('native:savefeatures', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results
    
        #######################################################################
        # Save vector features to file
        #######################################################################
        #Se guarda el raster_stats en format .csv
        #######################################################################
        
        alg_params = {
            'DATASOURCE_OPTIONS': '',
            'INPUT': 'Zonal_Statistics_90961545_cd97_4a17_8e85_1c091f1ffbc6',
            'LAYER_NAME': '',
            'LAYER_OPTIONS': '',
            'OUTPUT': '/Users/gonzalorigirozzi/Desktop/Clase 4/OUTPUT/raster_stats.csv',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['SaveVectorFeaturesToFile'] = processing.run('native:savefeatures', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}
        

    def name(self):
        return 'model3'

    def displayName(self):
        return 'model3'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Model3()
