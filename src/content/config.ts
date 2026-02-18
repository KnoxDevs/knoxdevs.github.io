import { defineCollection, z } from 'astro:content';

const linksSchema = z.object({
  website: z.string().optional().nullable(),
  email: z.string().optional().nullable(),
  github: z.string().optional().nullable(),
  twitter: z.string().optional().nullable(),
  meetup: z.string().optional().nullable(),
  slack: z.string().optional().nullable(),
  facebook: z.string().optional().nullable(),
}).optional().nullable();

const locationSchema = z.object({
  name: z.string().optional().nullable(),
  address: z.string().optional().nullable(),
  city_state: z.string().optional().nullable(),
  latitude: z.number().optional().nullable(),
  longitude: z.number().optional().nullable(),
}).optional().nullable();

const groups = defineCollection({
  type: 'data',
  schema: z.object({
    name: z.string(),
    description: z.string(),
    image: z.string().optional().nullable(),
    links: linksSchema,
    location: locationSchema,
    slack_channel: z.string().optional().nullable(),
  }),
});

const organizers = defineCollection({
  type: 'data',
  schema: z.object({
    name: z.string(),
    description: z.string().optional().nullable(),
    image: z.string().optional().nullable(),
    group: z.union([z.string(), z.array(z.string())]).optional().nullable(),
    links: linksSchema,
  }),
});

const conferences = defineCollection({
  type: 'data',
  schema: z.object({
    name: z.string(),
    description: z.string(),
    image: z.string().optional().nullable(),
    links: linksSchema,
    location: locationSchema,
  }),
});

const organizations = defineCollection({
  type: 'data',
  schema: z.object({
    name: z.string(),
    description: z.string(),
    image: z.string().optional().nullable(),
    links: linksSchema,
    location: locationSchema,
  }),
});

const spaces = defineCollection({
  type: 'data',
  schema: z.object({
    name: z.string(),
    type: z.string().optional().nullable(),
    description: z.string(),
    image: z.string().optional().nullable(),
    links: linksSchema,
    location: locationSchema,
  }),
});

export const collections = { groups, organizers, conferences, organizations, spaces };
