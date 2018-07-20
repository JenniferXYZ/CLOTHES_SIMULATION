using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using Obi;
using UnityEngineInternal;


namespace AutoGeneration
{
    //[ExecuteInEditMode]
    public class autotwoface : MonoBehaviour
    {

        // Use this for initialization
        private Shader shader;
        private Shader shader_backface;
        // public Texture texture;
        private Color materials_color;
        void Start()
        {
            SkinnedMeshRenderer cloth = this.GetComponent<SkinnedMeshRenderer>();
            GameObject tmp = this.gameObject;

            Debug.Log(tmp);
            // tmp.AddComponent<Material>();
            //MeshRenderer cloth=this.GetComponent<MeshRenderer>();
            // utilise setvalue to 
            // from the early step it is only one material often, then use this to produce another two materials.
            shader_backface = Resources.Load("shader/StandardBackfaces") as Shader;
            // materials_color = tmp.GetComponent<Material>().color;
            //cloth.materials.SetValue(2,2);
            Renderer rendertmp = tmp.GetComponent<Renderer>();
            materials_color = rendertmp.material.color;     //use renderer to find materials
            rendertmp.materials = new Material[2];
            rendertmp.materials[1].shader = shader_backface;
            rendertmp.materials[0].color = materials_color;
            rendertmp.materials[1].color = materials_color;
            //Debug.Log(rendertmp);
            //Obi.ObiActor.
        }
        // Update is called once per frame
        void Update() { }

    }







    //[ExecuteInEditMode]
    public class autocloth : MonoBehaviour
    {

        GameObject here;
        private void Awake()
        {

            // test_mesh();
            // changetoskinnedrender();
            // ObiCloth ss = new ObiCloth();
            //bool s = ss.Initializing;
        }
        // Use this for initialization
        IEnumerator wait()
        {
            yield return new WaitForSeconds(0.03f);
        }
        IEnumerator Start()
        {

            IEnumerator e = generatecloth();
            yield return e;
            if (!e.MoveNext()) // over the end
            {
                initialize_cloth_property();
                // StartCoroutine(wait());
                //EditorApplication.isPaused = true;
            }
            else
            {
                Debug.Log("Wrong Simulation!");
                EditorApplication.isPaused = true;
            }
            // add two side  all both side is clear need to be initialized
        }

        private void changetoskinnedrender()   //mesh render to skinned render
        {
            here = this.gameObject;
            here.AddComponent<SkinnedMeshRenderer>();
            SkinnedMeshRenderer skintmp = here.GetComponent<SkinnedMeshRenderer>();
            MeshRenderer tmp = here.GetComponent<MeshRenderer>();
            MeshFilter filtertmp = here.GetComponent<MeshFilter>();
            skintmp.sharedMesh = filtertmp.sharedMesh;
            tmp.enabled = false;

        }
        private void test_mesh()
        {

            // ObiMeshTopology.CreateInstance("meshtopology");
        }
        IEnumerator generatecloth()
        {
            here = this.gameObject;
            //Debug.Log(here.name);
            //Debug.Log(this.name);
            //ObiMeshTopology.CreateInstance("meshtopology");
            ObiMeshTopology meshtopology = ScriptableObject.CreateInstance<ObiMeshTopology>();
            meshtopology.InputMesh = here.GetComponent<MeshFilter>().sharedMesh;
            // Debug.Log(ss.InputMesh.name);
            meshtopology.Generate(); //for meshtoplogy

            GameObject solveroriginal = new GameObject();
            //get solver from the assets
            // solveroriginal.AddComponent<ObiSolver>();   
            here.AddComponent<ObiCloth>();
            ObiCloth tmp = here.GetComponent<ObiCloth>();
            //tmp.Solver.RelinquishRenderablePositions();
            tmp.SelfCollisions = true;
            //set solve parameters
            // or tmp.Solver = solveroriginal.AddComponent<ObiSolver>();

            tmp.Solver = solveroriginal.AddComponent<ObiSolver>();
            tmp.Solver.name = "Our Model Solver";
            tmp.Solver.maxParticles = 6000;
            tmp.Solver.volumeConstraintParameters.enabled = false;
            tmp.Solver.skinConstraintParameters.enabled = false;
            tmp.Solver.shapeMatchingConstraintParameters.enabled = false;
            tmp.Solver.tetherConstraintParameters.enabled = false;
            tmp.Solver.pinConstraintParameters.enabled = false;
            tmp.Solver.densityConstraintParameters.enabled = false;


            tmp.Solver.bendingConstraintParameters.evaluationOrder = Oni.ConstraintParameters.EvaluationOrder.Sequential;   //sequantial to reduce iterations amount
            tmp.Solver.distanceConstraintParameters.iterations = 6;
            tmp.Solver.bendingConstraintParameters.iterations = 6;
            tmp.Solver.collisionConstraintParameters.iterations = 6;
            tmp.Solver.shapeMatchingConstraintParameters.iterations = 6;
            tmp.Solver.stitchConstraintParameters.iterations = 6;
            tmp.Solver.particleCollisionConstraintParameters.iterations = 6;
            tmp.Solver.substeps = 2;
            //  tmp.Solver.
            tmp.SharedTopology = meshtopology;




            yield return tmp.StartCoroutine(tmp.GeneratePhysicRepresentationForMesh());
            tmp.AddToSolver(null);   //add constraints back

        }
        void initialize_cloth_property()
        {
            // bending constraints
            ObiBendingConstraints bend = this.GetComponent<ObiBendingConstraints>();
            bend.maxBending = 0f;
            // cancel some constraints
            ObiTetherConstraints tether = this.GetComponent<ObiTetherConstraints>();
            tether.enabled = false;
            ObiSkinConstraints skin = this.GetComponent<ObiSkinConstraints>();
            skin.enabled = false;
            ObiVolumeConstraints volume = this.GetComponent<ObiVolumeConstraints>();
            volume.enabled = false;
            ObiAerodynamicConstraints aero = this.GetComponent<ObiAerodynamicConstraints>();
            aero.enabled = false;

            ObiCloth tmp = this.GetComponent<ObiCloth>();
            tmp.SelfCollisions = true;
            tmp.CollisionMaterial = Resources.Load("collision_material/LowFriction") as ObiCollisionMaterial;


            //tmp.runInEditMode = true;  won't destroy after playing
            //unfix particle
            //for (int i = 0; i < tmp.invMasses.Length; i++) 
            //     tmp.invMasses[i]= 0; 


        }
        void manualpause()
        {

            if (Input.GetKeyDown(KeyCode.Space))
            {
                /* if (!EditorApplication.isPaused)
                        EditorApplication.isPaused = true;
                    else
                        EditorApplication.isPaused = false;
                        */
                /*if (Time.timeScale > 0)
                    Time.timeScale = 0;
                else
                    Time.timeScale = 1;
                    */
                if (EditorApplication.isPlaying == true)
                {
                    Debug.Log("sss");
                    Debug.Break();
                }
                else
                {
                    ///Debug.Log("sss");
                    EditorApplication.isPlaying = true;
                }
            }

        }
        // Update is called once per frame
        /*#if UNITY_EDITOR
            void Update()
            {
                // Debug.Log("Its time: " + Time.time);
                if (Application.isEditor && !Application.isPlaying)
                {
                    //do what you want
                    Debug.Log("Its time: " + Time.time);
                }
            }
        #endif
        */

        void Update()
        {
            // manualpause();

            if (Application.isPlaying)
            {
                if (Input.GetKeyDown(KeyCode.Space))
                {
                    Debug.Break();

                }
            }
            else
            {
                if (Input.GetKeyDown(KeyCode.Space))
                {
                    EditorApplication.isPaused = false;
                }

            }
            //if(Application.platform == RuntimePlatform.WindowsEditor)
            //     Debug.Log("Do something special here!");
        }

    }
}
